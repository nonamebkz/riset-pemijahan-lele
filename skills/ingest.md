# Keterampilan: Mengolah Sumber

Versi: 2
Lokasi: skills/ingest.md.
Baca AGENTS.md dan rules/schema.md sebelum menjalankan.

## Pemicu dan batas
Gunakan untuk sumber baru atau versi baru di raw/. Proses satu per satu kecuali pengguna menentukan lain. Jika hanya ada URL, minta pengguna menyimpan sumber lokal atau mengizinkan alur impor terpisah; keterampilan ini tidak menulis ke raw/.

## 0. Inisialisasi
Jalankan sebelum §1 jika struktur belum lengkap atau pengguna meminta inisialisasi.

**Direktori** (buat jika belum ada): `raw/`, `wiki/sources/`, `wiki/concepts/`, `wiki/analyses/`, `state/jobs/`.

**Berkas** (buat hanya jika belum ada; jangan timpa isi lama):
- `wiki/index.md` — judul Katalog Wiki; bagian Sumber, Konsep, Analisis (kosong boleh).
- `wiki/log.md` — judul Log Kegiatan.
- `state/sources.md` — judul Registri Sumber.

**Wiki versi sebelumnya:** jika ada halaman wiki tanpa frontmatter schema v2, layout/metadata lama, atau indeks tidak cocok dengan berkas di `wiki/`, dokumentasikan temuan di catatan job, **usulkan migrasi** (pemetaan ke schema v2), dan **hentikan migrasi massal** sampai pengguna menyetujui. Ingest sumber baru tetap boleh setelah init struktur, kecuali pengguna meminta fokus migrasi.

Setelah init, lanjut ke §1.

## 1. Identifikasi
- Baca registri, indeks, dan pekerjaan belum selesai.
- Periksa identitas karya, versi, nama lain, dan keterbacaan.
- Hitung hash hanya jika alat tersedia; jika tidak, bandingkan isi yang dapat dibaca dan catat metodenya.
- Sumber identik yang sudah complete dan tidak memiliki integrasi tertunda tidak perlu ditulis ulang. Laporkan dilewati.
- Jika ada pekerjaan partial untuk versi ini, lanjutkan pekerjaan itu setelah memeriksa file aktual. Jangan membuat pekerjaan duplikat.
- Versi berbeda menggunakan version_id baru. Bila identitas belum pasti, tandai dugaan duplikat sebelum menggabungkan.

## 2. Rencanakan
- Baca halaman konsep terkait, termasuk judul dan alias.
- Tentukan informasi baru, penguat, koreksi, pertentangan, dan batas ekstraksi.
- Buat job dengan cakupan, versi sumber, berkas terdampak, keadaan awal, dan langkah validasi.
- Tandai sumber processing dan job running setelah rencana tersimpan.
- Pisahkan perubahan yang boleh langsung dari usulan yang memerlukan persetujuan sesuai AGENTS.md.

## 3. Olah dan integrasikan
- Baca sumber selengkap cakupan yang disepakati; jangan mengklaim membaca gambar/halaman yang tidak dapat diakses.
- Buat atau perbarui ringkasan untuk versi sumber, dengan jejak ke bahan asli.
- Perbarui konsep relevan; jangan berhenti setelah ringkasan sumber selesai.
- Buat konsep baru hanya jika tidak sudah terwakili oleh judul/alias lain dan isinya cukup berguna.
- Rujuk klaim penting dekat dengan bukti; pertahankan periode, satuan, dan konteks.
- Catat konflik tanpa menimpa kesimpulan halaman yang sudah ditinjau. Simpan usulan perubahan substantif di job bila perlu izin.
- Terapkan revisi dan status tinjauan sesuai schema.
- Setelah setiap perubahan, perbarui langkah job agar dapat dilanjutkan. Sebelum menulis lagi, periksa tidak ada perubahan pihak lain.

## 4. Validasi
Periksa seluruh halaman yang berubah:
- Sumber dan versi benar; kutipan/lokasi bukti tidak dikarang.
- Klaim didukung atau diberi label ketidakpastian/sintesis.
- Tautan lokal valid dan halaman tercantum di indeks.
- Metadata, alias, status, dan revisi konsisten.
- Halaman terkait benar-benar telah dipertimbangkan.
- Raw tidak berubah, sejauh dapat diperiksa dengan sarana tersedia.
Catat pemeriksaan yang tidak bisa dilakukan; jangan menandainya lulus.

## 5. Tuntaskan
- Perbarui indeks dan registri sesuai hasil nyata.
- Jika ada integrasi penting atau persetujuan yang masih tertunda, gunakan partial/blocked, bukan complete.
- Konflik yang sudah dicatat lengkap dapat tetap menjadi hasil pemrosesan complete bila tidak menghambat cakupan integrasi.
- Tulis log, lalu tandai job complete hanya jika semua langkah wajib berhasil.
- Laporkan halaman dibuat/diubah, ketidakpastian, dan keputusan pengguna yang diperlukan.

## Jika terputus
Jangan mengulang dari awal secara buta. Baca job, registri, dan berkas terdampak. Cocokkan keadaan aktual, validasi langkah yang sudah selesai, lalu lanjutkan yang tersisa. Jangan menghapus hasil pihak lain untuk mengembalikan keadaan lama.

## Contoh pemanggilan
“Baca AGENTS.md, rules/schema.md, dan skills/ingest.md. Proses sumber baru di raw/ satu per satu. Lanjutkan pekerjaan yang terputus terlebih dahulu dan laporkan usulan yang memerlukan persetujuan.”

## Skill Cursor terkait
- Skill utama ingest: `.cursor/skills/llm-wiki-ingest/SKILL.md`
- Query: `.cursor/skills/llm-wiki-query/SKILL.md` + `skills/query.md`
- Maintain: `.cursor/skills/llm-wiki-maintain/SKILL.md` + `skills/maintain.md`
