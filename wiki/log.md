# Log Kegiatan

## 2026-09-29 — job-20260929-ingest-001

- **Jenis:** ingest (dua sumber raw)
- **Hasil:** inisialisasi wiki/state; halaman sumber dan konsep dibuat; registri diperbarui
- **Halaman:** 2 sumber, 5 konsep; indeks diperbarui
- **Validasi:** isi dibaca dari `raw/cara-merawat-air.md` dan `raw/pembahasan-kolam-terpal-dan-pemijahan.md`; hash SHA-256 dicatat; raw tidak diubah
- **Sisa:** tinjauan manusia belum; ukuran kolam di sumber pembahasan belum ditentukan (hanya rekomendasi wadah terpisah)

## 2026-09-29 — job-20260929-ingest-002

- **Jenis:** ingest (2 sumber baru; 2 sumber lama dilewati)
- **Hasil:** 2 halaman sumber; konsep baru perawatan kolam pasca pemijahan; konsep penetasan revision 2
- **Dilewati:** cara-merawat-air v1, pembahasan v1 (hash unchanged, complete)
- **Validasi:** hash SHA-256 dicatat; raw tidak diubah
- **Sisa:** tinjauan manusia; pertimbangkan rename berkas raw dengan spasi agar path lebih aman (opsional, butuh izin karena raw/)

## 2026-09-29 — job-20260929-ingest-003

- **Jenis:** ingest (2 sumber pH baru; 4 sumber lama dilewati)
- **Hasil:** 2 halaman sumber; konsep pengaturan pH; parameter kualitas air revision 2
- **Validasi:** raw tidak diubah

## 2026-09-29 — job-20260929-ingest-004

- **Jenis:** ingest (spesifikasi pemijahan baru; 6 sumber dilewati)
- **Hasil:** 1 sumber, 2 konsep baru; penetasan rev 3 (uncertain: waktu menetas); parameter rev 3 (tahap pemijahan)
- **Validasi:** raw tidak diubah

## 2026-09-29 — job-20260929-ingest-005

- **Jenis:** ingest (3 sumber baru; 7 dilewati)
- **Hasil:** jentik nyamuk, pakan larva, saran penetasan; 2 konsep baru; penetasan rev 4
- **Validasi:** raw tidak diubah

## 2026-09-29 — job-20260929-ingest-006

- **Jenis:** ingest (pasca-pemijahan baru; 10 dilewati)
- **Hasil:** 1 sumber; konsep alur pasca; induk rev 2; perawatan kolam rev 2; penetasan + source_ref pasca
- **Validasi:** raw tidak diubah

## 2026-09-29 — job-20260929-ingest-007

- **Jenis:** ingest (kakaban + layout aerasi; 11 dilewati)
- **Hasil:** 2 sumber; konsep layout aerasi; bak/kakaban rev 2 (uncertain ukuran lembar); penetasan diperkaya
- **Validasi:** raw tidak diubah

## 2026-09-29 — job-20260929-ingest-008

- **Jenis:** ingest (membedakan-telur + deep-research; 13 dilewati)
- **Hasil:** 2 halaman sumber; konsep seleksi telur; penetasan rev 5; induk rev 3; komposisi pakan rev 2
- **Integrasi:** usulan harmonisasi waktu tetas 24–30 h (+36 h toleransi) dan methylene blue non-default dari deep-research — **belum human-reviewed**
- **Validasi:** registri 15/15 raw complete; hash dicatat; raw tidak diubah; indeks diperbarui
- **Sisa:** tinjauan manusia untuk SOP tetas, methylene blue, bobot induk 300–800 g vs spesifikasi

## 2026-09-29 — job-20260929-ingest-009

- **Jenis:** ingest (hasil-riset-1.html baru; 15 dilewati)
- **Hasil:** 1 halaman sumber; konsep kriteria pra-pemijahan (sintesis web); induk rev 4; parameter air rev 4
- **Validasi:** hash SHA-256; raw tidak diubah; registri 16/16 complete
- **Sisa:** sitasi web tidak ada di raw HTML; rasio 1:2–1:3 vs spesifikasi 1:1; Ovaprim hanya literatur

## 2026-09-29 — job-20260929-ingest-010

- **Jenis:** ingest (hasil-riset-2.html baru; 16 dilewati)
- **Hasil:** 1 sumber; konsep unit inkubasi engineering; layout aerasi rev 2; penetasan rev 6
- **Validasi:** hash SHA-256; raw tidak diubah; registri 17/17 complete
- **Sisa:** skala debit studi 18 L vs kolam terpal; % exchange/hari telur; sitasi FAO/IPB kosong di HTML

## 2026-09-29 — job-20260929-ingest-011

- **Jenis:** ingest (hasil-riset-3.html baru; 17 dilewati)
- **Hasil:** 1 sumber; konsep metode pemijahan (sintesis web); induk rev 5; kriteria rev 2; penetasan rev 7
- **Validasi:** hash SHA-256; raw tidak diubah; registri 18/18 complete
- **Sisa:** dosis Ovaprim bervariasi; striping bukan SOP terpal; sitasi kosong di HTML

## 2026-09-29 — job-20260929-ingest-012

- **Jenis:** ingest (pakan-alternative.md baru; 18 dilewati)
- **Hasil:** 1 sumber; konsep pakan alternatif sintesis riset; komposisi pakan larva rev 3
- **Validasi:** hash SHA-256; raw tidak diubah; registri 19/19 complete
- **Sisa:** jurnal `[citation: N]` belum di raw; gap rucah/rebon/cacing vs praktik lapangan wiki

## 2026-09-29 — job-20260929-ingest-013

- **Jenis:** ingest (aerasi-kolam.md baru; 19 dilewati)
- **Hasil:** 1 sumber; layout aerasi rev 3; penetasan rev 8; unit inkubasi diperbarui (% exchange)
- **Validasi:** hash SHA-256; raw tidak diubah; registri 20/20 complete
- **Sisa:** 1–2 vs 4–6 batu aerasi; satuan udara vs air; DO lapangan belum terukur di wiki

## 2026-09-29 — job-20260929-ingest-014

- **Jenis:** ingest (blower.md baru; 20 dilewati)
- **Hasil:** 1 sumber; konsep kalibrasi DO/blower; layout aerasi rev 4
- **Validasi:** hash SHA-256; raw tidak diubah; registri 21/21 complete
- **Sisa:** log DO nyata di lapangan pengguna belum di wiki

## 2026-09-29 — job-20260929-ingest-015

- **Jenis:** ingest (cara cepat menetaskan telur.md baru; 21 dilewati)
- **Hasil:** 1 sumber; penetasan rev 9 (tabel suhu, golden setting 18–30 h)
- **Validasi:** hash SHA-256; raw tidak diubah; registri 22/22 complete
- **Catatan:** path raw berisi spasi (seperti berkas raw lain)

## 2026-09-29 — job-20260929-ingest-016

- **Jenis:** ingest (methylene blue.md baru; 22 dilewati)
- **Hasil:** 1 sumber; konsep MB inkubasi; penetasan rev 10
- **Validasi:** hash SHA-256; raw tidak diubah; registri 23/23 complete
- **Sisa:** kebijakan MB vs larangan telur-lele — butuh persetujuan manusia

## 2026-09-29 — job-20260929-ingest-017

- **Jenis:** ingest (info pemindahan induk.md baru; 23 dilewati)
- **Hasil:** 1 sumber; konsep pemindahan induk; alur pasca rev 2; induk rev 6
- **Validasi:** hash SHA-256; raw tidak diubah; registri 24/24 complete

## 2026-09-29 — job-20260929-ingest-018

- **Jenis:** ingest (estimasi waktu kawin.md baru; 24 dilewati)
- **Hasil:** 1 sumber; konsep durasi & indikator pijah; pemindahan induk rev 2; alur pasca rev 3; induk rev 7
- **Validasi:** hash SHA-256; raw tidak diubah; registri 25/25 complete
- **Sisa:** titik acuan «1–2 jam» mulai vs selesai pijah — butuh persetujuan manusia untuk SOP tunggal

## 2026-09-30 — job-20260930-maintain-001

- **Jenis:** maintain (audit bawaan)
- **Cakupan:** 25 sumber + 22 konsep; hash 25/25; 0 tautan rusak
- **Temuan:** indeks penetasan rev usang; gap alur end-to-end
- **Perbaikan:** tidak diterapkan

## 2026-09-30 — job-20260930-maintain-002

- **Jenis:** maintain (perbaikan tautan bukti raw → wiki/sources)
- **Hasil:** penetasan rev 11; alur pasca rev 4; pemindahan induk rev 3; durasi rev 2; layout rev 5; induk rev 8; MB rev 2; indeks
- **Validasi:** 0 tautan rusak pasca-edit
- **Sisa:** singkatan «raw §» di pakan-alternatif, kalibrasi-do, komposisi — batch berikutnya bila diminta

## 2026-09-30 — job-20260930-maintain-003

- **Jenis:** maintain (rename raw + alias registri; permintaan pengguna)
- **Hasil:** 14 berkas raw di-rename ke kebab-case/topik jelas; `state/sources.md` + 14 `wiki/sources` + catatan job; `raw/README.md`
- **Validasi:** hash 25/25 unchanged; `source_id` wiki tidak diubah

## 2026-09-30 — job-20260930-ingest-scan

- **Jenis:** ingest (pemindai; tidak ada sumber baru)
- **Hasil:** 25/25 raw `complete`; hash cocok; `raw/README.md` diabaikan (bukan sumber)
- **Perubahan wiki:** tidak ada
