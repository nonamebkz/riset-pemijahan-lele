---
id: src-blower-v1
type: source
title: Kalibrasi DO dan blower (catatan raw)
aliases: [throttling blower telur, DO meter pemijahan]
created: 2026-09-29
updated: 2026-09-29
revision: 1
review_status: unreviewed
reviewed_revision: null
reviewed_at: null
evidence_status: supported
tags: [aerasi, DO, blower, kalibrasi]
source_id: blower
version_id: v1
source_refs:
  - source_id: blower
    version_id: v1
---

# Kalibrasi DO dan blower (catatan raw)

## Identitas dan versi sumber

- **source_id:** blower
- **version_id:** v1
- **Bahan asli:** `raw/blower.md`
- **Hash:** SHA-256 `98addc1142509127724e0267fa01ee5001336fea1662d9382d852ebe422d159c`

## Cakupan pembacaan

Seluruh berkas (145 baris), 2026-09-29.

## Ringkasan

Metode **kalibrasi lapangan** DO vs blower untuk kolam pemijahan telur/larva. Target DO: telur **≥5 mg/L**; larva awal **5–7**; benih **>14 h** **4–6 mg/L**. Ukur **DO meter** di 3 titik (dekat kakaban, tengah, area arus); waktu **05–07** (DO terendah) dan **18–21**. Jika **DO <5**: +**20–30%** debit udara, tambah diffuser (4→6), bersihkan batu, kurangi kepadatan telur (contoh 20→26 L/menit). Jika **arus mengganggu** telur (kakaban geser, telur lepas, gelembung besar ke kakaban): **throttle** turunkan **30–50%** (contoh 40→20 L/menit), ukur ulang 30–60 menit; jangan matikan aerasi. Matriks: DO<5 arus aman → naikkan; DO>5 telur terganggu → turunkan; stabil → pertahankan. Layout: diffuser sisi, fine bubble, **valve per jalur**. SOP: cek DO **2×/hari**, penyesuaian bertahap **20–30%**, aerasi **24 jam**. Kesimpulan: **DO >5 tanpa turbulensi tinggi**—kalibrasi akhir = **DO terukur + respons fisik telur**.

## Klaim utama (lokasi di raw)

| Topik | Lokasi |
|-------|--------|
| Target DO per fase | ~9–25 |
| Tindakan DO rendah | ~31–55 |
| Indikator & koreksi arus kuat | ~59–102 |
| Layout & valve | ~106–128 |
| Standar operasional | ~131–139 |
| Kesimpulan | ~143–145 |

## Keterbatasan

- Panduan operasional raw; belum log pengukuran nyata di wiki.

## Halaman terkait

- [Kalibrasi DO dan blower pembenihan lele](../concepts/kalibrasi-do-dan-blower-pembenihan-lele.md)
- [Layout aerasi pembenihan lele](../concepts/layout-aerasi-pembenihan-lele.md)
- [Aerasi kolam v1](../sources/aerasi-kolam-v1.md)
