---
id: concept-kalibrasi-do-blower
type: concept
title: Kalibrasi DO dan blower pembenihan lele
aliases: [throttling blower, DO meter kakaban]
created: 2026-09-29
updated: 2026-09-30
revision: 2
review_status: unreviewed
reviewed_revision: null
reviewed_at: null
evidence_status: supported
tags: [DO, blower, aerasi, telur]
source_refs:
  - source_id: blower
    version_id: v1
  - source_id: aerasi-kolam
    version_id: v1
---

# Kalibrasi DO dan blower pembenihan lele

## Ringkasan

Prosedur lapangan untuk menjawab: **DO ≥5 mg/L tanpa arus yang melepas telur**. Sumber: [blower v1](../sources/blower-v1.md); desain awal blower/volume: [aerasi-kolam v1](../sources/aerasi-kolam-v1.md) + [Layout aerasi pembenihan lele](layout-aerasi-pembenihan-lele.md).

## Penjelasan

### Target DO ([Kalibrasi DO dan blower v1](../sources/blower-v1.md))

| Fase | Target |
|------|--------|
| Telur 0–3 hari | **≥ 5 mg/L** |
| Larva awal 3–14 hari | **5–7 mg/L** |
| Benih >14 hari | **4–6 mg/L** |

Selaras sasaran penetasan ~5 mg/L di wiki; larva/benih sedikit lebih fleksibel.

### Pengukuran

- **DO meter digital**; 3 titik: dekat kakaban, tengah kolam, area arus/keluaran.
- **2×/hari:** pagi **05–07** (DO minimum); sore **18–21** (kestabilan).

### DO rendah (<5 mg/L)

Indikasi: telur putih/mati ↑, larva di permukaan, gerak lambat.

| Tindakan | Detail |
|----------|--------|
| Naikkan blower | **+20–30%** debit udara (contoh 20→26 L/menit) |
| Diffuser | tambah titik (4→6) |
| Maintenance | bersihkan batu aerasi |
| Kepadatan | kurangi telur jika biomassa tinggi |

### Arus terlalu kuat (telur terganggu)

Indikasi: kakaban bergeser, telur lepas, telur menumpuk di satu sisi, gelembung besar ke kakaban.

**Jangan matikan aerasi** — kurangi debit via **valve** **30–50%** (contoh 40→20 L/menit); ukur ulang DO setelah **30–60 menit**.

| Kondisi | Aksi |
|---------|------|
| DO <5, arus aman | Naikkan 20–30% |
| DO >5, telur terganggu | Turunkan 30–50% |
| DO stabil, telur normal | Pertahankan |

Target akhir: **DO ≥5 mg/L**, kakaban bergerak **ringan**, telur menempel.

### Layout pendukung

Diffuser di **sisi** kolam; **fine bubble**; **valve per jalur**; hindari jet ke kakaban ([Kalibrasi DO dan blower v1](../sources/blower-v1.md) — raw baris 106–121; selaras [Aerasi kolam v1](../sources/aerasi-kolam-v1.md) sketsa layout).

## Bukti dan sumber

- [Blower v1](../sources/blower-v1.md)
- [Aerasi kolam v1](../sources/aerasi-kolam-v1.md)

## Hubungan

- [Layout aerasi pembenihan lele](layout-aerasi-pembenihan-lele.md)
- [Penetasan telur lele — praktik kolam terpal](penetasan-telur-lele-praktik-kolam-terpal.md)
- [Parameter kualitas air lele](parameter-kualitas-air-lele.md)
- [Seleksi dan ciri telur lele](seleksi-dan-ciri-telur-lele.md) — telur putih/mati

## Pertentangan dan ketidakpastian

- Target larva/benih **4–7 mg/L** vs grow-out **>3 mg/L** di parameter air—tahap berbeda.
- Angka ±20–30% / ±30–50% adalah panduan raw, bukan hasil uji A/B di kolam pengguna.

## Pertanyaan terbuka

- Merek/model DO meter & kalibrasi rutin di lapangan Anda.
