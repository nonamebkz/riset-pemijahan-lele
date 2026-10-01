---
name: llm-wiki-ingest
description: >-
  Mengolah sumber baru di raw/ ke wiki bukti-first (riset pemijahan lele).
  Memuat AGENTS.md, rules/schema.md, skills/ingest.md; inisialisasi struktur;
  usulkan migrasi wiki lama sebelum migrasi massal. Gunakan saat pengguna
  memproses raw/, ingest sumber, memasukkan dokumen ke wiki, atau menempel
  prompt ingest berulang project ini.
---

# LLM Wiki — ingest (skill utama)

## Prompt berulang (jalankan persis)

Baca AGENTS.md, rules/schema.md, dan skills/ingest.md. Inisialisasi struktur yang belum tersedia tanpa menimpa file lama. Jika ditemukan wiki versi sebelumnya, usulkan migrasi terlebih dahulu. Setelah itu, proses sumber di raw/ satu per satu sesuai batas izin.

## Rantai otomatis

1. **Rules** `.cursor/rules/llm-wiki-*.mdc` sudah aktif (core always-on; editing/raw saat berkas terkait).
2. **Baca** `AGENTS.md` → `rules/schema.md` → `skills/ingest.md`.
3. **Jalankan** `skills/ingest.md` §0 Inisialisasi, lalu §1–§5.
4. **Alat:** `python3 tools/wiki_check.py raw` (§1) dan `validate` (§4); jangan skrip sekali pakai.
5. **Alihkan** bila perlu:
   - pertanyaan tentang isi wiki → skill `llm-wiki-query` + `skills/query.md`
   - audit/tautan/registri → skill `llm-wiki-maintain` + `skills/maintain.md`

## Prompt pendek (setara)

- «Ingest raw»
- «Proses sumber di raw/»

Hasil harus sama dengan prompt berulang di atas.
