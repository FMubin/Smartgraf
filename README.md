# 📊 SMARTGRAF — BPS Kabupaten Pandeglang
### *Sistem Otomasi Publikasi Infografis & Naskah Interpretasi Statistik KCDA 7 Bab*

---

## 📖 Ringkasan
**SMARTGRAF** adalah platform otomatisasi terintegrasi yang dirancang khusus untuk mempermudah dan mempercepat penyusunan publikasi **Kecamatan Dalam Angka (KCDA)** untuk seluruh 35 kecamatan di **Kabupaten Pandeglang**. 

Aplikasi ini mencakup pembuatan infografis siap cetak ukuran A5, visualisasi perbandingan desa (14 Chart), penyusunan naskah interpretasi analisis statistik otomatis per bab, dan ekspor massal dalam format PDF A5, Word (.docx), serta PNG High Definition.

---

## ✨ Fitur Unggulan

1. **🏛️ Dashboard & Profil 35 Kecamatan**:
   - Ringkasan indikator strategis 7 Bab KCDA secara komprehensif.
   - Indikator status data, kelengkapan naskah, dan grafik per kecamatan aktif.

2. **📥 Pusat Data & Template**:
   - Format standar **Master KCDA Excel** dan **Merge CSV BPS** (7 Bab).
   - Pengunduhan template master dan import otomatis satu-klik.

3. **🎨 24 Preset Gaya & Template Desain**:
   - Beragam kategori gaya visual (*Formal BPS*, *Modern Glass*, *Cyber Tech*, *Nature & Eco*, *Minimalist*, *Luxury Gold*).
   - Penyesuaian skema warna gradien, model latar belakang (radial, mesh, cyber-grid), pola geografis/kontur topografi, bingkai ikon, tipografi font, dan transparansi kaca.

4. **✏️ Editor Isi Infografis KCDA (Bab 1 - 7)**:
   - Visualisasi interaktif tiap bab infografis A5.
   - Generator kode QR dinamis untuk verifikasi publikasi resmi BPS.
   - Tata letak kartu responsif dan kustomisasi judul bab dwi-bahasa (Indonesia & Inggris).

5. **📊 Studio Pemetaan Variabel & 14 Chart**:
   - Visualisasi grafik komparasi desa/kelurahan antar bab.
   - Salin grafik langsung ke clipboard atau unduh grafik beresolusi tinggi (PNG HD) untuk dokumen Word / InDesign.

6. **📝 Naskah Interpretasi Statistik Otomatis**:
   - Penyusunan ulasan dan narasi analisis data per bab secara otomatis.
   - Ekspor naskah lengkap 7 Bab ke format Microsoft Word (.docx).

7. **🚀 Pusat Ekspor & Cetak Massal**:
   - Ekspor instan per kecamatan atau pemrosesan batch massal untuk seluruh 35 kecamatan di Kabupaten Pandeglang.
   - Unduhan ZIP terpadu berisi PDF A5, Word Naskah, dan Gambar Infografis HD.

---

## 🚀 Cara Menjalankan

Aplikasi ini berbasis web client-side (HTML5, Vanilla JavaScript, CSS3 modern) yang dapat dijalankan secara langsung tanpa memerlukan server backend yang rumit:

1. Buka file `index.html` langsung di browser modern (Chrome, Edge, Firefox, Safari).
2. Atau jalankan skrip `run.bat` untuk membuka aplikasi secara otomatis.

---

## 📂 Struktur Proyek

```
infografis-generator/
│
├── index.html                  # Antarmuka utama aplikasi SMARTGRAF
├── app.js / app_v1.js          # Logika engine otomatisasi, chart, dan rendering
├── style.css                   # Styling desain, layout, dan tema antarmuka
├── logo bps.png                # Aset logo resmi Badan Pusat Statistik
├── master_kcda.xlsx            # Template Master Excel KCDA 7 Bab
├── Merge_01_2026.csv s.d 07    # Sampel data CSV Merge BPS 7 Bab
├── interpretasi.docx           # Sampel berkas naskah interpretasi
└── tabular_columns_def.json    # Definisi kolom variabel tiap bab
```

---

## 🏢 Hak Cipta & Instansi

Dikembangkan untuk **Badan Pusat Statistik (BPS) Kabupaten Pandeglang**  
*Mewujudkan Data Statistik Berkualitas untuk Perencanaan Pembangunan Daerah.*
