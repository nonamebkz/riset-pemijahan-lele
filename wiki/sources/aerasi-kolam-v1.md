---
id: src-aerasi-kolam-v1
type: source
title: Aerasi kolam terpal pemijahan (catatan raw)
aliases: [kalibrasi blower telur lele, water exchange larva]
created: 2026-09-29
updated: 2026-09-29
revision: 1
review_status: unreviewed
reviewed_revision: null
reviewed_at: null
evidence_status: supported
tags: [aerasi, kolam terpal, DO, pompa]
source_id: aerasi-kolam
version_id: v1
source_refs:
  - source_id: aerasi-kolam
    version_id: v1
---

# Aerasi kolam terpal pemijahan (catatan raw)

## Identitas dan versi sumber

- **source_id:** aerasi-kolam
- **version_id:** v1
- **Bahan asli:** `raw/aerasi-kolam.md`
- **Hash:** SHA-256 `cb24af00fbace8ef2d3f308e655767b325837bf9118f480ec9960031df759f19`

## Cakupan pembacaan

Seluruh berkas (209 baris), 2026-09-29.

## Ringkasan

Catatan **desain engineering** untuk kolam kakaban terpal fase telur/larva: asumsi **2×3 m**, air **40–50 cm** (~**3.000 L**), kepadatan telur ±10.000–30.000/kolam. Target DO **>5 mg/L**, suhu **26–30 °C**, pH **6,5–8**, arus lembut. **Aerasi udara:** **0,5–1 L udara/menit per 100 L** → **15–30 L/menit** (rekomendasi blower **20–40 L/menit**, tekanan **0,02–0,04 MPa**, **4–6** titik diffuser); layout ASCII 4 kakaban, batu **±20–30 cm** dari kakaban, tidak tepat di bawah telur. **Pertukaran air telur:** **0–5%/hari** (hari 0–2), **5–10%** (hari 3–5 menetas), larva **10–20%/hari** (5–14 h); contoh 5%/hari ≈ **0,10 L/menit** kontinu—praktik sering **sifon + refill manual**. **Flow-through alternatif:** **1–2% volume/jam** → **30–60 L/jam** (0,5–1 L/menit) untuk 3.000 L. Setup praktis: aerator **40 L/menit**, 4 batu, selang 6 mm, 24 jam; pompa celup **300–500 L/jam** intermittent 10–15 menit/jam. Prioritas: **DO tinggi & arus halus**, bukan ganti air besar saat telur.

## Klaim utama (lokasi di raw)

| Topik | Lokasi |
|-------|--------|
| Asumsi volume & target air | ~1–26 |
| Perhitungan L udara/menit | ~28–51 |
| Layout ASCII & jarak diffuser | ~55–81 |
| Tabel % ganti air per umur | ~94–100 |
| Debit pompa & flow-through | ~104–170 |
| Rekomendasi setup & kesimpulan | ~174–209 |

## Keterbatasan

- Angka desain dari satu catatan raw; belum uji lapangan terdokumentasi di wiki.
- Satuan **L/menit udara** (blower) ≠ **L/menit air** (flow-through/studi IPB).

## Halaman terkait

- [Layout aerasi pembenihan lele](../concepts/layout-aerasi-pembenihan-lele.md)
- [Penetasan telur lele — praktik kolam terpal](../concepts/penetasan-telur-lele-praktik-kolam-terpal.md)
- [Unit inkubasi telur lele — engineering (sintesis web)](../concepts/unit-inkubasi-telur-lele-engineering-sintesis-web.md)
