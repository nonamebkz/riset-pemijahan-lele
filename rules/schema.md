# Struktur Data Wiki

Versi: 2
Lokasi pemasangan: rules/schema.md.
Baca bersama AGENTS.md. Pedoman ini menentukan format; jangan menggandakan definisinya dalam keterampilan.

## Konvensi
Gunakan Markdown berbahasa Indonesia, nama berkas huruf kecil dengan tanda hubung, dan tautan relatif dari berkas yang memuatnya. Satu konsep utama per halaman. Cari judul dan alias sebelum membuat halaman. Jangan mengganti nama otomatis.
Tanggal menggunakan waktu lingkungan yang benar-benar tersedia dalam ISO 8601. Jika tidak tersedia, gunakan null; jangan menebak. Tanggal publikasi berbeda dari tanggal pemrosesan.
ID harus stabil dan unik dalam proyek. Gunakan pengenal acak jika sarana tersedia; jika tidak, alokasikan nomor urut setelah memeriksa registri dengan satu penulis aktif. Jangan turunkan ID hanya dari judul atau nama berkas.

## Metadata halaman wiki
Setiap halaman substantif memakai YAML frontmatter:
- id: pengenal halaman stabil.
- type: source | concept | analysis.
- title: judul.
- aliases: daftar sinonim; boleh kosong.
- created: tanggal pembuatan atau null.
- updated: tanggal perubahan terakhir atau null.
- revision: bilangan dimulai dari 1; bertambah saat isi berubah.
- review_status: unreviewed | human-reviewed | needs-review.
- reviewed_revision: revisi yang disetujui manusia, atau null.
- reviewed_at: tanggal persetujuan atau null.
- evidence_status: supported | uncertain | conflicting.
- tags: daftar, boleh kosong.
- source_refs: daftar pasangan source_id dan version_id, boleh kosong hanya jika tidak membuat klaim faktual.

Untuk type source, tambahkan source_id dan version_id milik sumber yang diringkas.
Supported berarti bukti yang dibaca mendukung isi dalam cakupannya, bukan jaminan kebenaran. Gunakan uncertain jika bukti belum cukup atau ekstraksi sebagian memengaruhi kesimpulan. Gunakan conflicting jika perbedaan bukti belum terselesaikan dan memengaruhi isi.
Status bukti tingkat halaman hanyalah ringkasan; tandai ketidakpastian dan konflik tepat di dekat klaim terkait.

## Tinjauan per revisi
Hanya persetujuan manusia yang dapat menetapkan human-reviewed. Simpan nomor revisi yang disetujui. Jika revisi berikutnya mengubah makna atau dasar bukti, ubah review_status menjadi needs-review dan pertahankan reviewed_revision sebelumnya. Catat persetujuan dan perubahan substantif dalam log.

## Bentuk halaman
Sumber: Identitas dan versi sumber; Cakupan pembacaan; Ringkasan; Klaim utama dan lokasi bukti; Keterbatasan; Halaman terkait.
Konsep: Ringkasan; Penjelasan; Bukti dan sumber; Hubungan; Pertentangan dan ketidakpastian; Pertanyaan terbuka.
Analisis: Pertanyaan; Jawaban; Dasar bukti; Sintesis/rekomendasi AI; Ketidakpastian; Halaman terkait.
Rujukan harus mengarah ke sumber asli atau ringkasan yang menautkan versi sumber asli secara jelas. Sertakan lokasi halaman/bagian/waktu bila tersedia. Jangan hanya mengandalkan daftar sumber di akhir untuk klaim yang ambigu.

## Identitas sumber dan versi
source_id mewakili karya/dokumen yang sama. version_id mewakili versi tertentu dari karya tersebut.
Jangan samakan berkas dengan karya: salinan identik dapat berbagi versi; revisi artikel menggunakan source_id yang sama dan version_id baru bila identitas karyanya dapat dipastikan.
Jika identitas belum pasti, tandai calon duplikat dan minta konfirmasi sebelum penggabungan. Hash membuktikan kesamaan byte, bukan otomatis kesamaan makna.
Sumber versi lama tidak ditimpa oleh agen. Jika pengguna mengganti isi sumber pada lokasi sama, tandai versi lama tidak lagi tersedia; minta salinan arsip bila dibutuhkan. Jangan membuat ulang sumber lama dari ringkasan AI.

## state/sources.md
Judul: Registri Sumber.
Satu bagian per source_id dan subbagian per version_id. Catat:
- Judul, penulis/penerbit, tanggal publikasi bila diketahui.
- Lokasi lokal dan URL asal jika tersedia.
- Hash beserta algoritma bila benar-benar dihitung; selain itu null.
- Alias lokasi jika ada salinan identik.
- processing_status: pending | processing | complete | partial.
- extraction_scope: full | partial | unavailable.
- Ringkasan sumber, job_id terakhir, halaman terdampak, kendala terbuka.
- Ketersediaan sumber: available | missing | replaced.
Complete berarti seluruh cakupan yang disepakati telah diintegrasikan dan divalidasi. Jika dokumen tidak dapat dibaca lengkap, status tetap partial kecuali pengguna secara eksplisit menyetujui cakupan terbatas; catat persetujuan tersebut. Pertentangan ilmiah tidak dengan sendirinya membuat pemrosesan partial.

## state/jobs/<job_id>.md
Satu catatan per pekerjaan penulisan, dibuat sebelum perubahan wiki.
Metadata: job_id, operation (ingest/query/lint/repair), status (planned/running/partial/blocked/complete), created, updated.
Bagian wajib:
- Tujuan, cakupan, dan izin pengguna.
- Sumber beserta versinya atau topik pertanyaan.
- Daftar berkas yang direncanakan berubah.
- Keadaan awal: revisi, hash, atau kutipan pembanding yang benar-benar dibaca.
- Daftar langkah: belum dikerjakan/sudah dikerjakan/divalidasi.
- Usulan yang memerlukan persetujuan.
- Hasil pemeriksaan, kendala, dan langkah berikutnya.
Berkas state dapat mengandung informasi sensitif; gunakan isi minimum yang diperlukan dan perlindungan akses proyek yang sama.

## Indeks dan log
wiki/index.md: kelompok Sumber, Konsep, Analisis; setiap halaman substantif memiliki satu tautan, judul, dan satu kalimat deskripsi. Jangan memasukkan state, index, atau log sebagai halaman pengetahuan.
wiki/log.md: tambah entri di akhir menggunakan tanggal tersedia dan job_id unik. Catat jenis kegiatan, hasil, halaman berubah, cakupan validasi, serta masalah tersisa. Entri gagal/sebagian tidak dihapus; catat kelanjutannya sebagai entri baru.
Jika tanggal tidak tersedia gunakan label tanggal-tidak-diketahui, bukan tanggal tebakan.
Log adalah riwayat. Status pekerjaan terkini berada pada catatan job, bukan disimpulkan hanya dari log.

## Penyelesaian dan pemulihan
Urutan: rencana tersimpan → perubahan isi → pemeriksaan → indeks/registri diperbarui → log hasil ditulis → job complete.
Jika terjadi kegagalan, tandai partial/blocked jika penulisan masih tersedia. Jika tidak bisa mencatat, laporkan kepada pengguna. Saat melanjutkan, cocokkan rencana dengan keadaan file nyata sebelum mengulangi langkah. Jangan menambah halaman/log duplikat hanya karena status terakhir tertinggal.

## Uji penerimaan skala kecil
1. Sumber sama dimasukkan dua kali: tidak ada halaman duplikat atau penulisan substantif yang tidak perlu.
2. Versi baru: hubungan versi terpelihara, bukti lama tidak hilang diam-diam.
3. Dua sumber berbeda pendapat: kedua posisi dan konteks dapat ditelusuri.
4. Pekerjaan terputus: bisa dilanjutkan berdasarkan keadaan aktual.
5. Pertanyaan lintas sumber: jawaban merujuk bukti dan memisahkan sintesis AI.
6. Perubahan halaman ditinjau: status tinjauan tidak melekat otomatis pada revisi baru.
