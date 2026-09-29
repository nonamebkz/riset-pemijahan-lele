---
id: concept-unit-inkubasi-engineering
type: concept
title: Unit inkubasi telur lele — engineering (sintesis web)
aliases: [hatch unit lele, trough inkubasi, debit aerasi telur]
created: 2026-09-29
updated: 2026-09-29
revision: 1
review_status: unreviewed
reviewed_revision: null
reviewed_at: null
evidence_status: uncertain
tags: [inkubasi, aerasi, flow-through, DO]
source_refs:
  - source_id: hasil-riset-2
    version_id: v1
---

# Unit inkubasi telur lele — engineering (sintesis web)

## Ringkasan

Merangkum **parameter layout/debit/DO** untuk wadah inkubasi telur dari [hasil-riset-2 v1](../sources/hasil-riset-2-v1.md). Melengkapi [Layout aerasi pembenihan lele](layout-aerasi-pembenihan-lele.md) (posisi batu/kakaban kolam terpal) dengan angka **flow-through**, **debit aerasi uji**, dan **dimensi tray** dari literatur yang dikutip sintesis—**bukan** SOP kolam terpal bila skala/wadah berbeda.

## Penjelasan

### Prinsip umum

- DO tinggi tanpa **hembusan langsung** ke gumpalan telur atau turbulensi ekstrem.
- Kombinasi **aerasi stabil** dan/atau **flow-through** (inlet–outlet) untuk hindari zona mati oksigen.
- Telur **menempel**—pemindahan dan arus kasar ↑ risiko lepas/rusak.

### Target DO (sintesis)

| Sumber dalam hasil-riset-2 | Patokan |
|----------------------------|---------|
| Praktis Indonesia (kutipan) | **> 5 mg/L** |
| FAO (kutipan) | **80–100% saturasi** telur/larva |
| Studi media air | **5,0–5,9 mg/L** terukur |

Selaras dengan sasaran ~5 mg/L di [Penetasan telur lele — praktik kolam terpal](penetasan-telur-lele-praktik-kolam-terpal.md).

### Flow-through — California trough (kutipan FAO)

- Volume trough **80–100 L** → aliran masuk **1–2 L/menit**, DO target **5–6 mg/L**.
- Jadwal menetas (25 °C): **28–32 jam** pasca fertilisasi (konteks hatchery, bukan kakaban terpal).
- **Larva awal** (konteks terkait): **3–5 L/menit** agar DO ≥ 5 mg/L.

Layout: inlet/outflow satu sisi; tray berlubang agar telur tidak hanyut saat sirkulasi.

### Debit aerasi — studi IPB (kutipan)

- Wadah: **18 L**; kepadatan **55 telur/L**.
- Perlakuan: **5 / 10 / 15 L/menit** vs tanpa aerasi → **5 L/menit** hatching/survival terbaik dalam studi ini.
- Implikasi: **kontrol debit** (flowmeter/katup), bukan aerator semaksimal mungkin.

### Tray + tangki (kutipan semi-artificial)

- Tray **50×60 cm**, frame PVC, mesh **2 mm**.
- Tangki sirkular **1,5 m³**, kedalaman air **40 cm**; aerasi kontinu + flow-through.
- Menetas ~**22 jam** (satu studi)—tambah variasi waktu di wiki penetasan.

### Kedalaman & posisi aerasi

- Contoh **40 cm** kedalaman dengan tray di dalam tangki—cukup untuk sirkulasi DO, kurangi jet dangkal ke telur.
- Aliran **halus/laminar**; risiko **mechanical agitation** menurunkan hatchability (kutip spesies lain dalam sintesis).

## Bukti dan sumber

- [Hasil riset 2 v1](../sources/hasil-riset-2-v1.md)

## Hubungan

- [Layout aerasi pembenihan lele](layout-aerasi-pembenihan-lele.md)
- [Penetasan telur lele — praktik kolam terpal](penetasan-telur-lele-praktik-kolam-terpal.md)
- [Parameter kualitas air lele](parameter-kualitas-air-lele.md)
- [Seleksi dan ciri telur lele](seleksi-dan-ciri-telur-lele.md)

## Pertentangan dan ketidakpastian

- **Kedalaman bak:** ~**20–30 cm** (saran penetasan kolam terpal) vs **40 cm** (studi tray tangki)—tipe wadah berbeda.
- **Waktu menetas:** **22 h**, **28–32 h @ 25 °C** (FAO/studi) vs rentang lapangan wiki—lihat konsep penetasan.
- Debit **5 L/menit/18 L** tidak linear ke kolam terpal besar tanpa rekayasa ulang.
- % **pertukaran air/hari** fase telur: **0–5%/hari** (telur awal) dicatat di [aerasi-kolam v1](../sources/aerasi-kolam-v1.md) untuk kolam terpal ~3.000 L—konteks berbeda dari trough hatchery.

## Pertanyaan terbuka

- Apakah kolam Anda memakai kakaban terpal saja vs trough/tray hatchery?
- Dokumen FAO/studi IPB asli akan disimpan di `raw/` untuk verifikasi sitasi?
