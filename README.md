# 📊 Supermarket Sales Dashboard - PySide6

## 👤 Informasi Mahasiswa
* **Nama:** Samsul Rizal
* **NIM:** F1D02310025
* **Kelas:** D

## 📖 Deskripsi Singkat
Project ini adalah aplikasi Desktop berbasis GUI untuk memvisualisasikan data penjualan supermarket secara interaktif. Dibangun menggunakan kombinasi **PySide6** (untuk antarmuka), **Pandas** (untuk pengolahan data), dan **Matplotlib** (untuk pembuatan grafik). Aplikasi ini mengadopsi desain dashboard analitik modern dengan kartu ringkasan (summary cards), filter dinamis, dan integrasi grafik yang tertanam langsung di dalam aplikasi (tidak membuka *window* terpisah).

## 💾 Sumber Data (Kaggle Dataset)
Aplikasi ini menggunakan dataset nyata dari Kaggle untuk memastikan visualisasi data lebih realistis:
* **Link Dataset:** [Supermarket Sales Dataset](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

**Penjelasan Singkat Isi Dataset:**
Dataset ini merekam data transaksi historis dari 3 cabang supermarket yang berbeda (Cabang A, B, dan C) selama 3 bulan. 
Beberapa kolom utama yang diolah dalam dashboard ini meliputi:
* `Branch`: Lokasi cabang supermarket (digunakan sebagai fitur filter data).
* `Product line`: Kategori barang yang dibeli oleh pelanggan (seperti *Health and beauty*, *Electronic accessories*, dll). Digunakan untuk analisis pada Bar Chart.
* `Customer type`: Mengkategorikan pelanggan menjadi *Member* (anggota) dan *Normal* (non-anggota). Digunakan untuk analisis distribusi pada Pie Chart.
* `Sales` / `Total`: Total nilai transaksi belanja. Digunakan untuk menghitung kartu ringkasan pendapatan.
* `Rating`: Penilaian kepuasan pelanggan dari skala 1-10.

## ✨ Fitur Utama
1. **Summary Cards:** 3 Kartu ringkasan interaktif yang menampilkan Total Penjualan, Total Transaksi, dan Rata-rata Rating secara *real-time* berdasarkan filter.
2. **Dual Filter Dinamis:** Pengguna dapat menyaring data dan grafik berdasarkan **Cabang (Branch)** dan **Kategori Produk (Product Line)**.
3. **Data Table:** Menampilkan data mentah CSV dalam bentuk tabel (`QTableWidget`) berdesain bersih tanpa garis *grid* yang kaku.
4. **Matplotlib Integration:** * **Bar Chart:** Visualisasi total penjualan berdasarkan kategori produk.
   * **Pie Chart:** Visualisasi persentase distribusi tipe pelanggan (*Member* vs *Normal*).
5. **Export Chart:** Fitur untuk menyimpan grafik visualisasi ke dalam format gambar (`.png`).
6. **Responsive & Modern UI:** Menggunakan `QSplitter` agar layout fleksibel saat di-*resize*, dipadukan dengan kustomisasi gaya (QSS) untuk tampilan modern (*flat design*).
