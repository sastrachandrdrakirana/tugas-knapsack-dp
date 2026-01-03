# LAPORAN TUGAS ALGORITMA
# 0/1 Knapsack Problem dengan Dynamic Programming

---

## Informasi Kelompok
SASTRA CHANDRA KIRANA .A (105841103721)
SAYA SENDIRI


| | |
|---|---|
| **Mata Kuliah** | Desain dan AnalisisAlgoritma |
| **Tugas** | 0/1 Knapsack Problem dengan Dynamic Programming |
| **Anggota 1** | [Sastra Chandra Kirana .A] |
| **Anggota 2** | [-] |
| **Tanggal deadline** | 04 Januari 2026 |

---

## Data Kasus: 10 Item Indomie

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

**Kapasitas Tas (Knapsack)**: 400 gram

---

# BAGIAN 1 - ANALISIS MASALAH

## 1.1 Identifikasi Jenis Knapsack

Jenis Knapsack yang digunakan dalam tugas ini adalah **0/1 Knapsack Problem**.

### Karakteristik 0/1 Knapsack:

1. **Binary Choice (Pilihan Biner)**
   - Setiap item hanya memiliki dua pilihan: **diambil (1)** atau **tidak diambil (0)**
   - Tidak ada opsi untuk mengambil sebagian item (fractional)

2. **Contoh dalam Kasus Ini**:
   - Kita tidak bisa mengambil "setengah bungkus" Indomie Goreng Original
   - Pilihan hanya: ambil 1 bungkus utuh, atau tidak sama sekali

3. **Perbedaan dengan Fractional Knapsack**:
   | Aspek | 0/1 Knapsack | Fractional Knapsack |
   |-------|--------------|---------------------|
   | Pilihan | Ambil semua atau tidak | Bisa ambil sebagian |
   | Metode Optimal | Dynamic Programming | Greedy Algorithm |
   | Kompleksitas | O(n × W) | O(n log n) |

## 1.2 Alasan Penggunaan Dynamic Programming

### Mengapa Dynamic Programming?

**1. Optimal Substructure (Struktur Optimal)**
   - Solusi optimal untuk masalah keseluruhan dapat dibangun dari solusi optimal sub-masalah
   - Jika kita tahu solusi optimal untuk item pertama, kita juga harus bisa menentukan solusi untuk item tersebut

**2. Overlapping Subproblems (Sub-masalah yang Tumpang Tindih)**
   - Dalam penyelesaian rekursif, sub-masalah yang sama dihitung berulang kali
   - DP menyimpan hasil perhitungan untuk menghindari redundansi

**3. Perbandingan Metode**:

```
┌─────────────────────────────────────────────────────────────┐
│           PERBANDINGAN METODE PENYELESAIAN                  │
├─────────────────────────────────────────────────────────────┤
│  Metode          │ Kompleksitas │ Untuk n=10, W=400        │
├─────────────────────────────────────────────────────────────┤
│  Brute Force     │ O(2^n)       │ 1,024 kombinasi          │
│  Rekursif (Memo) │ O(n × W)     │ 4,000 operasi            │
│  DP Tabulasi     │ O(n × W)     │ 4,000 operasi            │
└─────────────────────────────────────────────────────────────┘
```

**4. Keuntungan DP**:
   - ✅ Menjamin solusi optimal
   - ✅ Efisien untuk ukuran masalah sedang
   - ✅ Dapat di-trace back untuk mendapatkan item terpilih
   - ✅ Tidak menghitung ulang sub-masalah yang sama

---

# BAGIAN 2 - STATE SPACE TREE

## 2.1 Penjelasan Node dan Level

### Definisi Node:
- **Node** merepresentasikan sebuah **state** atau keadaan dalam proses pengambilan keputusan
- Setiap node menyimpan informasi:
  - Item yang sedang dipertimbangkan
  - Total berat saat ini
  - Total nilai saat ini
  - Sisa kapasitas

### Definisi Level:
- **Level** menunjukkan **item ke berapa** yang sedang dipertimbangkan
- Level 0: Root (belum ada keputusan)
- Level 1: Keputusan untuk Item 1 (Indomie Goreng Original)
- Level 2: Keputusan untuk Item 2 (Indomie Goreng Rendang)
- Dan seterusnya...

### Struktur Tree:
```
Level 0 (Root)     : Kondisi awal, kapasitas = 400g, nilai = 0
Level 1 (Item 1)   : Keputusan ambil/tidak Indomie Goreng Original
Level 2 (Item 2)   : Keputusan ambil/tidak Indomie Goreng Rendang
Level 3 (Item 3)   : Keputusan ambil/tidak Indomie Goreng Pedas
Level 4 (Item 4)   : Keputusan ambil/tidak Indomie Kuah Soto
...
Level 10 (Item 10) : Keputusan ambil/tidak Indomie Iga Penyet
```

## 2.2 State Space Tree (Hingga Level 4)

```
                                    [ROOT]
                            Kapasitas: 400g, Nilai: 0
                                      │
                 ┌────────────────────┴────────────────────┐
                 │                                         │
        [AMBIL Item 1]                            [TIDAK AMBIL Item 1]
    Indomie Goreng Original                      Kapasitas: 400g
    Berat: 85g, Nilai: 90                        Nilai: 0
    Sisa: 315g, Total: 90                              │
                 │                                     │
         ┌───────┴───────┐                    ┌────────┴────────┐
         │               │                    │                 │
   [AMBIL Item 2]  [TIDAK Item 2]       [AMBIL Item 2]   [TIDAK Item 2]
   Rendang +91g     Sisa: 315g          Rendang +91g      Sisa: 400g
   Sisa: 224g       Nilai: 90           Sisa: 309g        Nilai: 0
   Nilai: 185                           Nilai: 95
         │               │                    │                 │
    ┌────┴────┐     ┌────┴────┐         ┌────┴────┐       ┌────┴────┐
    │         │     │         │         │         │       │         │
 [+Item3] [-Item3] [+Item3] [-Item3] [+Item3] [-Item3] [+Item3] [-Item3]
 Sisa:139  Sisa:224 Sisa:230 Sisa:315 Sisa:224 Sisa:309 Sisa:315 Sisa:400
 Nilai:270 Nilai:185 Nilai:175 Nilai:90 Nilai:180 Nilai:95 Nilai:85 Nilai:0
    │         │        │        │        │         │        │        │
   ...       ...      ...      ...      ...       ...      ...      ...
   
Level 4: Keputusan untuk Item 4 (Indomie Kuah Soto, 75g, nilai 80)
```

### Tabel State pada Setiap Level:

| Level | Item | Keputusan | Berat Diambil | Sisa Kapasitas | Total Nilai |
|-------|------|-----------|---------------|----------------|-------------|
| 0 | - | - | 0 | 400 | 0 |
| 1 | Goreng Original (85g, 90) | Ambil | 85 | 315 | 90 |
| 2 | Goreng Rendang (91g, 95) | Ambil | 176 | 224 | 185 |
| 3 | Goreng Pedas (85g, 85) | Ambil | 261 | 139 | 270 |
| 4 | Kuah Soto (75g, 80) | Ambil | 336 | 64 | 350 |

## 2.3 Contoh Pruning

### Apa itu Pruning?
Pruning adalah teknik memangkas cabang-cabang tree yang **tidak mungkin** menghasilkan solusi optimal, sehingga mengurangi jumlah node yang perlu dieksplorasi.

### Jenis Pruning pada Knapsack:

**1. Feasibility Pruning (Pruning Kelayakan)**
- Memangkas cabang jika **berat melebihi kapasitas**

```
Contoh:
- Pada path: Ambil Item 1 (85g) → Ambil Item 2 (91g) → Ambil Item 3 (85g)
- Total berat = 261g, Sisa kapasitas = 139g
- Jika Item 9 (Jumbo, 120g) dipilih: 261 + 120 = 381g ✓ (masih valid)
- Tetapi jika dilanjutkan mengambil lebih banyak, akan melebihi 400g
- Cabang yang melebihi 400g di-PRUNE (dipangkas)
```

**2. Bound Pruning (Pruning Batas Atas)**
- Memangkas cabang jika **estimasi nilai maksimum** tidak lebih baik dari solusi terbaik saat ini

```
Ilustrasi Pruning:

                    [Node A]
                 Nilai saat ini: 185
                 Sisa kapasitas: 224g
                 Upper Bound: 450
                        │
            ┌───────────┴───────────┐
            │                       │
       [AMBIL]                  [TIDAK]
    Upper Bound: 420          Upper Bound: 380
    → Lanjutkan               → PRUNE jika best > 380
            │                       │
           ...                     ✂️ (dipangkas)
```

### Contoh Konkret Pruning:

```
Misalkan best_solution = 400 (dari jalur lain)

Path yang sedang dieksplorasi:
- Tidak ambil Item 1, Tidak ambil Item 2, Tidak ambil Item 3, Tidak ambil Item 4
- Total nilai = 0, Sisa kapasitas = 400g
- Item tersisa: 5,6,7,8,9,10 dengan total nilai = 75+92+88+98+100+93 = 546
- Tetapi total berat = 70+90+85+100+120+91 = 556g > 400g

Upper bound dengan fractional: 
- Ambil semaksimal mungkin dari item tersisa
- Estimasi upper bound ≈ 450

Jika upper_bound (450) > best_solution (400):
  → Lanjutkan eksplorasi

Jika upper_bound < best_solution:
  → PRUNE! ✂️
```

---

# BAGIAN 3 - IMPLEMENTASI

## 3.1 Kode Program Python

Program diimplementasikan dalam file `knapsack_dp.py`. Berikut adalah komponen utama:

### Struktur Program:

```python
# Data Input
item_names = [
    "Indomie Goreng Original",
    "Indomie Goreng Rendang",
    "Indomie Goreng Pedas",
    "Indomie Kuah Soto",
    "Indomie Kuah Ayam Bawang",
    "Indomie Goreng Aceh",
    "Indomie Hype Abis Ayam Geprek",
    "Indomie Salted Egg",
    "Indomie Goreng Jumbo",
    "Indomie Mi Goreng Iga Penyet"
]

weights = [85, 91, 85, 75, 70, 90, 85, 100, 120, 91]  # gram
values = [90, 95, 85, 80, 75, 92, 88, 98, 100, 93]    # kepuasan
capacity = 400  # gram
```

### Algoritma Utama:

```python
def knapsack_dp(weights, values, capacity, item_names):
    n = len(weights)
    
    # Inisialisasi tabel DP (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Mengisi tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]  # Tidak ambil
            else:
                dp[i][w] = max(
                    dp[i-1][w],  # Tidak ambil
                    values[i-1] + dp[i-1][w - weights[i-1]]  # Ambil
                )
    
    return dp[n][capacity], dp
```

### Backtracking untuk Item Terpilih:

```python
def get_selected_items(dp, weights, values, capacity, item_names):
    n = len(weights)
    w = capacity
    selected_items = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append((item_names[i-1], weights[i-1], values[i-1]))
            w -= weights[i-1]
    
    return selected_items
```

## 3.2 Output Program

### Hasil Eksekusi:

```
======================================================================
       0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING
              Studi Kasus: Varian Indomie
======================================================================

======================================================================
DATA ITEM INDOMIE
======================================================================
No  Nama Item                          Berat (g)   Nilai     
----------------------------------------------------------------------
1   Indomie Goreng Original            85          90        
2   Indomie Goreng Rendang             91          95        
3   Indomie Goreng Pedas               85          85        
4   Indomie Kuah Soto                  75          80        
5   Indomie Kuah Ayam Bawang           70          75        
6   Indomie Goreng Aceh                90          92        
7   Indomie Hype Abis Ayam Geprek      85          88        
8   Indomie Salted Egg                 100         98        
9   Indomie Goreng Jumbo               120         100       
10  Indomie Mi Goreng Iga Penyet       91          93        
----------------------------------------------------------------------
KAPASITAS TAS:                         400 gram
======================================================================

======================================================================
HASIL OPTIMASI 0/1 KNAPSACK
======================================================================

📦 NILAI MAKSIMUM KEPUASAN: 418

⚖️  TOTAL BERAT: 400 gram dari 400 gram kapasitas

📊 KAPASITAS TERPAKAI: 100.0%

----------------------------------------------------------------------
DAFTAR ITEM TERPILIH:
----------------------------------------------------------------------
No  Nama Item                          Berat (g)   Nilai     
----------------------------------------------------------------------
1   Indomie Goreng Original            85          90        
3   Indomie Goreng Pedas               85          85        
4   Indomie Kuah Soto                  75          80        
5   Indomie Kuah Ayam Bawang           70          75        
7   Indomie Hype Abis Ayam Geprek      85          88        
----------------------------------------------------------------------
TOTAL                                  400         418       
======================================================================
```
---

# BAGIAN 4 - ANALISIS

## 4.1 Mengapa Kombinasi Tersebut Optimal?

### Item yang Terpilih:

| No | Item | Berat | Nilai | Rasio (Nilai/Berat) |
|----|------|-------|-------|---------------------|
| 1 | Indomie Goreng Original | 85g | 90 | 1.06 |
| 3 | Indomie Goreng Pedas | 85g | 85 | 1.00 |
| 4 | Indomie Kuah Soto | 75g | 80 | 1.07 |
| 5 | Indomie Kuah Ayam Bawang | 70g | 75 | 1.07 |
| 7 | Indomie Hype Abis Ayam Geprek | 85g | 88 | 1.04 |
| **TOTAL** | | **400g** | **418** | |

### Alasan Optimalitas:

**1. Memaksimalkan Penggunaan Kapasitas**
   - Total berat: 400g dari 400g (100% kapasitas)
   - Kapasitas terpakai sepenuhnya, tidak ada ruang tersisa

**2. Kombinasi Nilai Tertinggi**
   - Tidak ada kombinasi lain dengan total ≤ 400g yang menghasilkan nilai > 418
   - DP menjamin ini dengan mengevaluasi semua kemungkinan valid

**3. Trade-off yang Tepat**
   - Meskipun beberapa item memiliki nilai lebih tinggi (seperti Salted Egg dengan nilai 98), kombinasi ini memberikan total nilai maksimum dengan memanfaatkan kapasitas penuh

**4. Bukti dari Tabel DP**
   - dp[10][400] = 418 adalah nilai maksimum yang dicapai
   - Ini adalah hasil dari semua perhitungan optimal sebelumnya

### Mengapa Bukan Kombinasi Lain?

**Alternatif 1**: Mengambil Indomie Goreng Jumbo (120g, nilai 100)
- Jika Jumbo diambil + item lain maksimal:
  - Jumbo (120) + Rendang (91) + Aceh (90) + Salted Egg (100) = 401g > 400g ❌
  - Jumbo (120) + Rendang (91) + Aceh (90) + Iga Penyet (91) = 392g ✓
  - Nilai = 100 + 95 + 92 + 93 = 380 < 470 ❌

**Alternatif 2**: Greedy by Value
- Ambil item dengan nilai tertinggi dulu:
  - Jumbo (100) + Salted Egg (98) + Rendang (95) + Iga Penyet (93) = 402g > 400g ❌
  - Tidak valid!

## 4.2 Perbandingan dengan Brute Force

### Konsep Brute Force:

```
Brute Force mengevaluasi SEMUA kemungkinan kombinasi:
- Untuk setiap item: 2 pilihan (ambil atau tidak)
- Total item: 10
- Total kombinasi: 2^10 = 1,024 kombinasi
```

### Pseudocode Brute Force:

```python
def brute_force_knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []
    
    # Coba semua 2^n kombinasi
    for mask in range(2**n):
        total_weight = 0
        total_value = 0
        combination = []
        
        for i in range(n):
            if mask & (1 << i):  # Bit ke-i aktif = ambil item i
                total_weight += weights[i]
                total_value += values[i]
                combination.append(i)
        
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = combination
    
    return max_value, best_combination
```

### Perbandingan Kompleksitas:

| Aspek | Brute Force | Dynamic Programming |
|-------|-------------|---------------------|
| **Kompleksitas Waktu** | O(2^n) | O(n × W) |
| **Kompleksitas Ruang** | O(n) | O(n × W) atau O(W) |
| **Untuk n=10, W=400** | 1,024 kombinasi | 4,000 operasi |
| **Untuk n=20, W=400** | 1,048,576 kombinasi | 8,000 operasi |
| **Untuk n=30, W=400** | ~1 miliar kombinasi | 12,000 operasi |

### Waktu Eksekusi Estimasi:

```
Asumsi: 1 juta operasi per detik

┌──────────────┬─────────────────────┬─────────────────────┐
│ Jumlah Item  │ Brute Force         │ Dynamic Programming │
├──────────────┼─────────────────────┼─────────────────────┤
│ n = 10       │ ~0.001 detik        │ ~0.004 detik        │
│ n = 20       │ ~1 detik            │ ~0.008 detik        │
│ n = 30       │ ~17.9 menit         │ ~0.012 detik        │
│ n = 40       │ ~12.7 hari          │ ~0.016 detik        │
│ n = 50       │ ~35.7 tahun         │ ~0.020 detik        │
└──────────────┴─────────────────────┴─────────────────────┘
```

### Kesimpulan Perbandingan:

1. **Brute Force**:
   - ✅ Sederhana dan mudah dipahami
   - ✅ Selalu menemukan solusi optimal
   - ❌ Tidak praktis untuk n besar (eksponensial)

2. **Dynamic Programming**:
   - ✅ Efisien untuk n dan W moderat
   - ✅ Selalu menemukan solusi optimal
   - ✅ Dapat di-trace back
   - ❌ Memerlukan memori O(n × W)

---

# KESIMPULAN

1. **Jenis Knapsack**: 0/1 Knapsack Problem karena setiap item hanya bisa diambil utuh atau tidak sama sekali

2. **Metode**: Dynamic Programming dipilih karena efisien dan menjamin solusi optimal

3. **Hasil Optimal**:
   - Nilai Maksimum: **418**
   - Item Terpilih: 5 item (Original, Pedas, Kuah Soto, Ayam Bawang, Hype Abis)
   - Total Berat: **400 gram** (100% kapasitas)

4. **Efisiensi**: DP lebih efisien dari Brute Force untuk kasus yang lebih besar

---

**Link GitHub**: [Akan diisi setelah upload]

**Link Pengumpulan**: https://forms.gle/R81RPhCD1DMtTsZa6
