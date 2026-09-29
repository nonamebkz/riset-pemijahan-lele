# Keterampilan: Memeriksa dan Merawat Wiki

Versi: 2
Lokasi: skills/maintain.md.
Baca AGENTS.md dan rules/schema.md terlebih dahulu.

## Mode
- Audit: bawaan. Tidak mengubah halaman pengetahuan; membuat job dan log pemeriksaan.
- Audit hanya-baca: jika diminta, tidak menulis apa pun, termasuk job/log. Laporan diberikan dalam percakapan.
- Perbaikan: jika diminta, terapkan hanya perubahan yang diizinkan AGENTS.md. Penghapusan, penggabungan, penggantian nama, dan perubahan kesimpulan halaman ditinjau memerlukan persetujuan khusus.
Jangan menafsirkan persetujuan audit sebagai persetujuan semua perbaikan.

## Persiapan
Tentukan cakupan halaman dan jenis pemeriksaan. Periksa pekerjaan belum selesai. Jika akan menulis, buat job dengan keadaan awal dan izin. Jangan mengubah job aktif milik penulis lain tanpa koordinasi.

## Pemeriksaan struktur
- Cocokkan berkas wiki dengan indeks; temukan halaman hilang atau tidak terdaftar.
- Periksa tautan lokal beserta penanda bagian bila dapat dilakukan. Bedakan tautan luar yang belum diperiksa dari tautan yang terbukti rusak.
- Cari konsep/analisis tanpa tautan masuk bermakna dari halaman lain; tautan indeks saja belum cukup.
- Cari calon duplikat berdasarkan judul, alias, identitas, dan isi. Jangan menggabungkan hanya karena judul mirip.
- Periksa metadata wajib, ID unik, revisi, dan format tanggal. Jangan mengarang nilai historis yang hilang.

## Pemeriksaan registri dan pekerjaan
- Cocokkan sumber aktual dengan registri, versi, dan ringkasannya.
- Cari sumber belum diproses, sumber hilang/diganti, serta hash yang tidak cocok jika perhitungan tersedia.
- Periksa job partial/blocked dan apakah pekerjaan aktual sudah lebih maju daripada catatannya.
- Periksa sumber complete yang masih memiliki integrasi tertunda.
- Periksa ekstraksi partial yang dinyatakan complete tanpa cakupan terbatas yang disetujui.
- Periksa source_refs menuju versi yang benar.
- Jangan memperbaiki identitas/versi secara massal tanpa rencana dan persetujuan.

## Pemeriksaan isi dan tinjauan
- Klaim penting memiliki bukti yang benar-benar mendukungnya.
- Sintesis AI dibedakan dari isi sumber.
- Pertentangan dilengkapi kedua bukti, periode, definisi, dan konteks.
- Klaim lama ditinjau berdasarkan bukti baru; usia dokumen saja tidak membuktikan salah.
- Ringkasan AI tidak dihitung sebagai bukti independen.
- Status human-reviewed mempunyai bukti persetujuan dan reviewed_revision yang sesuai.
- Perubahan makna setelah persetujuan memicu needs-review.
- Konsep dan pertanyaan terbuka yang penting belum terabaikan.
Jangan melakukan pencarian luar otomatis. Usulkan sumber tambahan jika perlu.

## Laporan temuan
Setiap temuan berisi tingkat (tinggi/sedang/rendah), lokasi, bukti, dampak, usulan tindakan, dan kebutuhan persetujuan. Pisahkan temuan terkonfirmasi dari dugaan.
Tinggi: bukti salah, klaim menyesatkan, hilangnya jejak sumber, atau perubahan tanpa izin.
Sedang: integrasi belum selesai, konflik belum dijelaskan, duplikasi, atau tautan penting rusak.
Rendah: format dan kerapian tanpa perubahan makna.
Laporkan cakupan nyata: halaman diperiksa, pemeriksaan dilakukan, dan bagian belum diperiksa. Jangan menyatakan seluruh wiki bersih dari pemeriksaan sampel.

## Perbaikan
1. Dapatkan izin yang diperlukan dan catat dalam job.
2. Baca ulang keadaan berkas; berhenti bila ada perubahan pihak lain yang berbenturan.
3. Terapkan perubahan kecil. Pertahankan jejak klaim lama dan bukti.
4. Terapkan revisi/status tinjauan sesuai schema.
5. Perbarui indeks/registri jika relevan.
6. Periksa ulang temuan dan tautan terdampak.
7. Tulis log hasil dan tuntaskan job, atau catat sisa pekerjaan.

## Uji penerimaan
Saat pengguna meminta pengujian alur, gunakan enam skenario di rules/schema.md. Jalankan pada salinan proyek atau data uji yang jelas, dengan izin pengguna. Jangan sengaja memutus proses atau mengubah sumber produksi hanya untuk simulasi.

## Contoh pemanggilan
“Periksa wiki sesuai skills/maintain.md dalam mode audit hanya-baca. Fokus pada status tinjauan, duplikasi sumber, dan pekerjaan yang belum selesai.”
“Perbaiki indeks dan tautan yang targetnya pasti. Sajikan usulan terpisah untuk perubahan substantif.”
