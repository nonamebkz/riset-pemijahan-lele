# Keterampilan: Menjawab dari Wiki

Versi: 2
Lokasi: skills/query.md.
Baca AGENTS.md dan rules/schema.md terlebih dahulu.

## Alur jawaban
1. Pahami pertanyaan, cakupan, dan periode waktunya. Nyatakan asumsi berisiko rendah bila diperlukan.
2. Baca indeks, lalu cari halaman relevan melalui judul, alias, dan teks.
3. Baca halaman yang relevan; perhatikan revisi, keadaan bukti, dan status tinjauan.
4. Periksa sumber asli untuk angka, kutipan langsung, klaim penentu, atau konflik. Perhatikan versi sumber dan ketersediaannya.
5. Jawab dengan rujukan yang dapat ditelusuri. Pisahkan klaim sumber, sintesis AI, dan rekomendasi.
6. Jika sumber tidak dapat diperiksa, nyatakan dasar jawaban yang sebenarnya. Jangan mengaku memeriksa sumber dari membaca ringkasan saja.
7. Sebutkan kekurangan bukti dan sumber yang dibutuhkan. Jangan diam-diam menjadikan pengetahuan model atau hasil web sebagai bukti koleksi.
8. Jangan mengirim isi pribadi ke layanan luar tanpa izin.

## Penyimpanan hasil eksplorasi
Jawaban berguna dapat memperkaya wiki, tetapi penyimpanan halaman analisis harus diminta pengguna atau sudah diizinkan secara tetap. Jika belum diizinkan, jawab dahulu dan tawarkan penyimpanan hanya bila bernilai.
Sebelum menyimpan:
- Cari analisis serupa dan konsep terkait.
- Buat job query sebelum mengubah berkas.
- Tentukan apakah membuat halaman baru atau memperbarui draf yang sudah ada.
- Ikuti izin perubahan pada halaman yang sudah ditinjau.
- Gunakan struktur analisis di schema, source_refs dengan versi, dan rujukan bukti asli.
- Jangan menghitung jawaban AI sebagai sumber independen yang menguatkan kesimpulannya sendiri.
- Perbarui indeks, periksa tautan dan bukti, tulis log, lalu tuntaskan job.

## Catatan kegiatan
Secara bawaan, pertanyaan biasa cukup dijawab tanpa mengubah berkas. Jika pengguna mengaktifkan pencatatan pertanyaan, buat job kecil dan log topik minimal; jangan menyimpan teks sensitif lengkap. Jika pengguna meminta hanya-baca, jangan menulis job atau log.

## Jika ditemukan kesalahan
Tunjukkan bukti dan pengaruhnya pada jawaban. Jangan diam-diam mengganti kesimpulan utama. Untuk perbaikan, gunakan skills/maintain.md dengan izin yang sesuai. Peringatan konflik boleh ditambahkan hanya jika penulisan memang diizinkan dan dicatat sebagai pekerjaan.

## Kriteria selesai
Jawaban menjawab pertanyaan, bukti bisa ditelusuri, batas cakupan jelas. Jika hasil disimpan, semua perubahan tercatat, indeks mutakhir, dan pemeriksaan wajib selesai; jika tidak, catat partial.

## Contoh pemanggilan
“Baca pedoman dan skills/query.md. Jawab berdasarkan wiki dengan rujukan. Hanya-baca; jangan simpan atau mencatat pertanyaan.”
“Jawab berdasarkan wiki lalu simpan analisis sebagai draf. Ikuti aturan tinjauan dan hindari duplikasi.”
