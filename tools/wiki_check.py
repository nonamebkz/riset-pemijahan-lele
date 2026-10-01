#!/usr/bin/env python3
"""Pemeriksa mekanis wiki (hanya baca). Jangan menulis ke raw/."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
REGISTRY = ROOT / "state" / "sources.md"
JOBS = ROOT / "state" / "jobs"
SKIP_RAW = {".gitkeep", "README.md"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
HASH_RE = re.compile(r"SHA-256 `([0-9a-f]{64})`", re.I)
LOKASI_RE = re.compile(r"\*\*Lokasi lokal:\*\*\s*`([^`]+)`")
ALIAS_RE = re.compile(r"\*\*Alias lokasi:\*\*\s*`([^`]+)`")
STATUS_RE = re.compile(r"\*\*status:\*\*\s*(\S+)", re.I)
SKIP_HREF_PREFIX = ("http://", "https://", "mailto:", "#")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("-") or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def knowledge_pages() -> list[Path]:
    pages: list[Path] = []
    for folder in ("sources", "concepts", "analyses"):
        d = WIKI / folder
        if d.is_dir():
            pages.extend(sorted(d.glob("*.md")))
    return pages


def wiki_md_files() -> list[Path]:
    extra = [WIKI / "index.md"]
    log = WIKI / "log.md"
    if log.exists():
        extra.append(log)
    return knowledge_pages() + extra


def resolve_href(src: Path, href: str) -> tuple[Path | None, str | None]:
    target_s = href.split("#", 1)[0].strip()
    if not target_s:
        return None, None
    target = (src.parent / target_s).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None, "outside"
    return target, None


def cmd_hash(paths: list[str]) -> int:
    code = 0
    for raw in paths:
        path = Path(raw)
        if not path.is_absolute():
            path = (ROOT / path).resolve()
        if not path.exists():
            print(f"MISSING {path}")
            code = 1
            continue
        print(f"{sha256_file(path)}  {path.relative_to(ROOT)}")
    return code


def parse_registry() -> list[dict]:
    if not REGISTRY.exists():
        return []
    text = REGISTRY.read_text(encoding="utf-8")
    entries: list[dict] = []
    source_id = None
    version_id = None
    buf: list[str] = []

    def flush() -> None:
        if source_id is None or version_id is None:
            return
        block = "\n".join(buf)
        hashes = HASH_RE.findall(block)
        lokasi = LOKASI_RE.findall(block)
        aliases = ALIAS_RE.findall(block)
        paths = [p for p in lokasi if p.startswith("raw/")]
        avail = None
        m = re.search(r"\*\*Ketersediaan:\*\*\s*(\S+)", block)
        if m:
            avail = m.group(1).strip()
        status = None
        m = re.search(r"\*\*processing_status:\*\*\s*(\S+)", block)
        if m:
            status = m.group(1).strip()
        entries.append(
            {
                "source_id": source_id,
                "version_id": version_id,
                "hashes": hashes,
                "paths": paths,
                "aliases": [p for p in aliases if p.startswith("raw/")],
                "availability": avail,
                "processing_status": status,
            }
        )

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            source_id = line[3:].strip()
            version_id = None
            buf = []
            continue
        if line.startswith("### ") and source_id:
            flush()
            version_id = line[4:].strip()
            buf = [line]
            continue
        if version_id is not None:
            buf.append(line)
    flush()
    return entries


def raw_files() -> list[Path]:
    if not RAW.is_dir():
        return []
    return sorted(
        p
        for p in RAW.iterdir()
        if p.is_file() and p.name not in SKIP_RAW
    )


def cmd_raw() -> int:
    entries = parse_registry()
    files = raw_files()
    file_hashes = {p.name: sha256_file(p) for p in files}
    registered_names: set[str] = set()
    code = 0

    print("=== raw vs registri ===")
    print(f"raw_files {len(files)}")
    print(f"registry_versions {len(entries)}")

    for e in entries:
        names = [Path(p).name for p in e["paths"]]
        registered_names.update(names)
        if e["availability"] != "available":
            continue
        raw_names = [n for n in names if n not in SKIP_RAW]
        if not raw_names:
            continue
        for name in raw_names:
            path = RAW / name
            if not path.exists():
                print(f"MISSING_FILE {e['source_id']}/{e['version_id']} expected raw/{name}")
                code = 1
                continue
            actual = file_hashes.get(name)
            if e["hashes"] and actual not in e["hashes"]:
                print(
                    f"HASH_MISMATCH {e['source_id']}/{e['version_id']} "
                    f"raw/{name} registry={e['hashes'][0]} actual={actual}"
                )
                code = 1
            elif not e["hashes"]:
                print(f"HASH_NULL {e['source_id']}/{e['version_id']} raw/{name}")

    for p in files:
        if p.name not in registered_names:
            print(f"NEW {p.relative_to(ROOT)} {file_hashes[p.name]}")

    if code == 0:
        print("RAW_OK")
    return code


def cmd_validate() -> int:
    pages = knowledge_pages()
    check_files = wiki_md_files()
    broken: list[tuple[str, str]] = []
    outside: list[tuple[str, str]] = []
    for p in check_files:
        if not p.exists():
            continue
        for _label, href in LINK_RE.findall(p.read_text(encoding="utf-8")):
            href = href.strip()
            if href.startswith(SKIP_HREF_PREFIX):
                continue
            target, err = resolve_href(p, href)
            if err == "outside":
                outside.append((str(p.relative_to(ROOT)), href))
                continue
            if target is None:
                continue
            if not target.exists():
                broken.append((str(p.relative_to(ROOT)), href))

    index = WIKI / "index.md"
    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    hrefs = [h.split("#", 1)[0] for _t, h in LINK_RE.findall(index_text)]
    dup = [k for k, v in Counter(hrefs).items() if v > 1]
    rels = [str(p.relative_to(WIKI)) for p in pages]
    missing = [r for r in rels if r not in hrefs]

    print("=== tautan & indeks ===")
    print(f"sources {len(list((WIKI / 'sources').glob('*.md')))}")
    print(f"concepts {len(list((WIKI / 'concepts').glob('*.md')))}")
    analyses = WIKI / "analyses"
    print(f"analyses {len(list(analyses.glob('*.md'))) if analyses.is_dir() else 0}")
    if broken:
        print("BROKEN")
        for src, href in broken:
            print(f"  {src} -> {href}")
    else:
        print("BROKEN []")
    if outside:
        print("OUTSIDE")
        for src, href in outside:
            print(f"  {src} -> {href}")
    print(f"DUP_INDEX {dup}")
    print(f"MISSING_INDEX {missing}")
    ok = not broken and not dup and not missing
    print("VALIDATE_OK" if ok else "VALIDATE_FAIL")
    return 0 if ok else 1


def cmd_pages() -> int:
    required = (
        "id",
        "type",
        "title",
        "revision",
        "review_status",
        "evidence_status",
    )
    ids: dict[str, list[str]] = defaultdict(list)
    missing_fm: list[str] = []
    missing_fields: list[str] = []
    type_mismatch: list[str] = []
    folder_type = {"sources": "source", "concepts": "concept", "analyses": "analysis"}
    incoming: dict[str, list[str]] = defaultdict(list)
    pages = knowledge_pages()
    by_resolve = {p.resolve(): p for p in pages}

    for p in pages + ([WIKI / "index.md"] if (WIKI / "index.md").exists() else []):
        text = p.read_text(encoding="utf-8")
        for _t, href in LINK_RE.findall(text):
            href = href.strip()
            if href.startswith(SKIP_HREF_PREFIX):
                continue
            target, err = resolve_href(p, href)
            if err or target is None:
                continue
            dest = by_resolve.get(target.resolve())
            if dest and dest != p:
                incoming[str(dest.relative_to(ROOT))].append(str(p.relative_to(ROOT)))

    print("=== halaman ===")
    code = 0
    for p in pages:
        rel = str(p.relative_to(ROOT))
        meta = parse_frontmatter(p.read_text(encoding="utf-8"))
        if not meta:
            missing_fm.append(rel)
            code = 1
            continue
        pid = meta.get("id", "")
        if pid:
            ids[pid].append(rel)
        for key in required:
            if key not in meta or meta[key] == "":
                missing_fields.append(f"{rel} missing {key}")
                code = 1
        expected = folder_type.get(p.parent.name)
        if expected and meta.get("type") and meta["type"] != expected:
            type_mismatch.append(f"{rel} type={meta.get('type')} expected={expected}")
            code = 1

    dups = {k: v for k, v in ids.items() if len(v) > 1}
    if dups:
        print("DUP_ID")
        for k, v in dups.items():
            print(f"  {k}: {', '.join(v)}")
        code = 1
    if missing_fm:
        print("NO_FRONTMATTER", missing_fm)
    if missing_fields:
        print("MISSING_FIELDS")
        for row in missing_fields:
            print(f"  {row}")
    if type_mismatch:
        print("TYPE_MISMATCH")
        for row in type_mismatch:
            print(f"  {row}")

    orphans = []
    index_only = []
    for p in pages:
        rel = str(p.relative_to(ROOT))
        srcs = incoming.get(rel, [])
        if not srcs:
            orphans.append(rel)
        elif srcs == ["wiki/index.md"] or set(srcs) <= {"wiki/index.md"}:
            index_only.append(rel)
    print(f"ORPHANS {orphans}")
    print(f"INDEX_ONLY {index_only}")
    print("PAGES_OK" if code == 0 else "PAGES_FAIL")
    return code


def cmd_jobs() -> int:
    print("=== jobs ===")
    if not JOBS.is_dir():
        print("NO_JOBS_DIR")
        return 0
    open_jobs: list[str] = []
    for path in sorted(JOBS.glob("job-*.md")):
        text = path.read_text(encoding="utf-8")
        m = STATUS_RE.search(text)
        status = m.group(1) if m else "unknown"
        if status != "complete":
            open_jobs.append(f"{path.name} {status}")
    if open_jobs:
        print("OPEN")
        for row in open_jobs:
            print(f"  {row}")
    else:
        print("OPEN []")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pemeriksa wiki proyek (hanya baca; tidak menulis raw/)."
    )
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("raw", help="hash raw/ vs state/sources.md")
    sub.add_parser("validate", help="tautan lokal + kelengkapan indeks")
    sub.add_parser("pages", help="frontmatter, id unik, yatim tautan")
    sub.add_parser("jobs", help="job yang belum complete")
    p_hash = sub.add_parser("hash", help="SHA-256 satu atau lebih berkas")
    p_hash.add_argument("paths", nargs="+")
    sub.add_parser("all", help="raw + validate + pages + jobs")
    args = parser.parse_args()
    cmd = args.cmd or "all"
    if cmd == "hash":
        return cmd_hash(args.paths)
    runners = {
        "raw": [cmd_raw],
        "validate": [cmd_validate],
        "pages": [cmd_pages],
        "jobs": [cmd_jobs],
        "all": [cmd_raw, cmd_validate, cmd_pages, cmd_jobs],
    }
    code = 0
    for fn in runners[cmd]:
        code = max(code, fn())
    return code


if __name__ == "__main__":
    sys.exit(main())
