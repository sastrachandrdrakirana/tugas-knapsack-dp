# 0/1 Knapsack Problem - Dynamic Programming
## Tugas Algoritma: Studi Kasus Varian Indomie

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic%20Programming-green.svg)]()

---

## 📋 Deskripsi

Program ini mengimplementasikan algoritma **0/1 Knapsack Problem** menggunakan **Dynamic Programming** untuk menyelesaikan masalah optimasi pemilihan varian Indomie dengan kapasitas tas terbatas.

### Studi Kasus
Memilih kombinasi optimal dari 10 varian Indomie untuk dimasukkan ke dalam tas dengan kapasitas maksimum **400 gram**, dengan tujuan memaksimalkan nilai kepuasan.

---

## 📦 Data Item

| No | Nama Item | Berat (gram) | Nilai Kepuasan |
|----|-----------|--------------|----------------|
| 1 | Indomie Goreng Original | 85 | 90 |
| 2 | Indomie Goreng Rendang | 91 | 95 |
| 3 | Indomie Goreng Pedas | 85 | 85 |
| 4 | Indomie Kuah Soto | 75 | 80 |
| 5 | Indomie Kuah Ayam Bawang | 70 | 75 |
| 6 | Indomie Goreng Aceh | 90 | 92 |
| 7 | Indomie Hype Abis Ayam Geprek | 85 | 88 |
| 8 | Indomie Salted Egg | 100 | 98 |
| 9 | Indomie Goreng Jumbo | 120 | 100 |
| 10 | Indomie Mi Goreng Iga Penyet | 91 | 93 |

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.x

### Eksekusi
```bash
python knapsack_dp.py
```

---

## 📊 Hasil Optimal

| Metrik | Nilai |
|--------|-------|
| **Nilai Maksimum** | 418 |
| **Total Berat** | 400 gram |
| **Kapasitas Terpakai** | 100% |

### Item Terpilih:
1. Indomie Goreng Original (85g, nilai 90)
2. Indomie Goreng Pedas (85g, nilai 85)
3. Indomie Kuah Soto (75g, nilai 80)
4. Indomie Kuah Ayam Bawang (70g, nilai 75)
5. Indomie Hype Abis Ayam Geprek (85g, nilai 88)

---

## 📁 Struktur File

```
TUGAS ALGORITMA/
├── knapsack_dp.py       # Program utama
├── laporan_knapsack.md  # Laporan lengkap (4 bagian)
└── README.md            # File ini
```

---

## 📖 Isi Laporan

Laporan mencakup 4 bagian:

1. **Analisis Masalah** - Identifikasi jenis Knapsack dan alasan penggunaan DP
2. **State Space Tree** - Visualisasi tree dengan node, level, dan pruning
3. **Implementasi** - Kode Python dengan output lengkap
4. **Analisis** - Penjelasan optimalitas dan perbandingan dengan Brute Force

---

## 👥 Kelompok

| Nama | NIM |
|------|-----|
| [Sastra Chandra Kirana .A] | [105841103721] |
| [-] | [-] |

---

## 📚 Referensi

- Cormen, T. H., et al. *Introduction to Algorithms* (CLRS)
- Knapsack Problem - Wikipedia

---

**Mata Kuliah**: Algoritma  
**Deadline**: 04 Januari 2026, 23:59
