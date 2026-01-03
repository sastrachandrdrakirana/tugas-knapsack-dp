"""
=============================================================================
TUGAS ALGORITMA: 0/1 KNAPSACK PROBLEM DENGAN DYNAMIC PROGRAMMING
=============================================================================
Program ini mengimplementasikan algoritma 0/1 Knapsack menggunakan 
Dynamic Programming untuk menyelesaikan masalah pemilihan item Indomie
dengan kapasitas tas terbatas.

Kelompok: [Nama Kelompok]
Anggota:
1. [Nama Anggota 1]
2. [Nama Anggota 2]
=============================================================================
"""

def knapsack_dp(weights, values, capacity, item_names):
    """
    Implementasi 0/1 Knapsack menggunakan Dynamic Programming.
    
    Parameters:
    - weights: list of int, berat masing-masing item
    - values: list of int, nilai kepuasan masing-masing item
    - capacity: int, kapasitas maksimum tas
    - item_names: list of str, nama masing-masing item
    
    Returns:
    - max_value: int, nilai maksimum yang bisa didapat
    - dp_table: 2D list, tabel DP untuk analisis
    """
    n = len(weights)
    
    # Inisialisasi tabel DP dengan ukuran (n+1) x (capacity+1)
    # dp[i][w] = nilai maksimum dengan i item pertama dan kapasitas w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Mengisi tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Jika berat item ke-i lebih besar dari kapasitas saat ini
            if weights[i-1] > w:
                # Tidak mengambil item ke-i
                dp[i][w] = dp[i-1][w]
            else:
                # Pilih maksimum antara:
                # 1. Tidak mengambil item ke-i: dp[i-1][w]
                # 2. Mengambil item ke-i: values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(dp[i-1][w], 
                              values[i-1] + dp[i-1][w - weights[i-1]])
    
    return dp[n][capacity], dp


def get_selected_items(dp, weights, values, capacity, item_names):
    """
    Backtracking untuk mendapatkan item-item yang terpilih.
    
    Parameters:
    - dp: 2D list, tabel DP
    - weights: list of int, berat masing-masing item
    - values: list of int, nilai masing-masing item
    - capacity: int, kapasitas tas
    - item_names: list of str, nama masing-masing item
    
    Returns:
    - selected_items: list of tuples (nama, berat, nilai)
    - total_weight: int, total berat item terpilih
    """
    n = len(weights)
    w = capacity
    selected_items = []
    
    # Backtracking dari dp[n][capacity]
    for i in range(n, 0, -1):
        # Jika nilai berbeda dengan baris sebelumnya, item ke-i dipilih
        if dp[i][w] != dp[i-1][w]:
            selected_items.append((item_names[i-1], weights[i-1], values[i-1], i))
            w -= weights[i-1]
    
    # Urutkan berdasarkan nomor item
    selected_items.sort(key=lambda x: x[3])
    
    # Hitung total berat
    total_weight = sum(item[1] for item in selected_items)
    
    return selected_items, total_weight


def print_dp_table(dp, weights, capacity, item_names):
    """
    Menampilkan tabel DP (sebagian untuk visualisasi).
    """
    n = len(weights)
    
    print("\n" + "=" * 70)
    print("TABEL DYNAMIC PROGRAMMING (Sebagian)")
    print("=" * 70)
    
    # Tampilkan header
    print(f"{'Item':<25}", end="")
    # Tampilkan beberapa kolom kapasitas
    sample_capacities = [0, 70, 85, 150, 200, 300, 400]
    sample_capacities = [c for c in sample_capacities if c <= capacity]
    
    for c in sample_capacities:
        print(f"W={c:<5}", end="")
    print()
    print("-" * 70)
    
    # Tampilkan baris
    for i in range(n + 1):
        if i == 0:
            print(f"{'(kosong)':<25}", end="")
        else:
            name = item_names[i-1][:22] + "..." if len(item_names[i-1]) > 22 else item_names[i-1]
            print(f"{name:<25}", end="")
        
        for c in sample_capacities:
            print(f"{dp[i][c]:<7}", end="")
        print()


def print_header():
    """Menampilkan header program."""
    print("=" * 70)
    print("       0/1 KNAPSACK PROBLEM - DYNAMIC PROGRAMMING")
    print("              Studi Kasus: Varian Indomie")
    print("=" * 70)


def print_data(item_names, weights, values, capacity):
    """Menampilkan data item."""
    print("\n" + "=" * 70)
    print("DATA ITEM INDOMIE")
    print("=" * 70)
    print(f"{'No':<4}{'Nama Item':<35}{'Berat (g)':<12}{'Nilai':<10}")
    print("-" * 70)
    
    for i, (name, weight, value) in enumerate(zip(item_names, weights, values), 1):
        print(f"{i:<4}{name:<35}{weight:<12}{value:<10}")
    
    print("-" * 70)
    print(f"{'KAPASITAS TAS:':<39}{capacity} gram")
    print("=" * 70)


def print_result(max_value, selected_items, total_weight, capacity):
    """Menampilkan hasil optimasi."""
    print("\n" + "=" * 70)
    print("HASIL OPTIMASI 0/1 KNAPSACK")
    print("=" * 70)
    
    print(f"\n📦 NILAI MAKSIMUM KEPUASAN: {max_value}")
    print(f"⚖️  TOTAL BERAT: {total_weight} gram dari {capacity} gram kapasitas")
    print(f"📊 KAPASITAS TERPAKAI: {(total_weight/capacity)*100:.1f}%")
    
    print("\n" + "-" * 70)
    print("DAFTAR ITEM TERPILIH:")
    print("-" * 70)
    print(f"{'No':<4}{'Nama Item':<35}{'Berat (g)':<12}{'Nilai':<10}")
    print("-" * 70)
    
    for i, (name, weight, value, _) in enumerate(selected_items, 1):
        print(f"{i:<4}{name:<35}{weight:<12}{value:<10}")
    
    print("-" * 70)
    print(f"{'TOTAL':<39}{total_weight:<12}{max_value:<10}")
    print("=" * 70)


def compare_with_brute_force(n):
    """Menampilkan perbandingan dengan brute force."""
    print("\n" + "=" * 70)
    print("PERBANDINGAN DENGAN BRUTE FORCE")
    print("=" * 70)
    
    brute_force_combinations = 2 ** n
    dp_operations = n * 400  # n × W
    
    print(f"""
┌─────────────────────────────────────────────────────────────────────┐
│                    ANALISIS KOMPLEKSITAS                            │
├─────────────────────────────────────────────────────────────────────┤
│  Metode              │ Kompleksitas    │ Operasi untuk n={n:<2}        │
├─────────────────────────────────────────────────────────────────────┤
│  Brute Force         │ O(2^n)          │ {brute_force_combinations:,} kombinasi          │
│  Dynamic Programming │ O(n × W)        │ {dp_operations:,} operasi              │
├─────────────────────────────────────────────────────────────────────┤
│  Efisiensi DP        │ {brute_force_combinations/dp_operations:.1f}x lebih cepat                            │
└─────────────────────────────────────────────────────────────────────┘
    """)


def main():
    """Fungsi utama program."""
    
    # =========================================================================
    # DATA KASUS: 10 ITEM INDOMIE
    # =========================================================================
    item_names = [
        "Indomie Goreng Original",      # 1
        "Indomie Goreng Rendang",       # 2
        "Indomie Goreng Pedas",         # 3
        "Indomie Kuah Soto",            # 4
        "Indomie Kuah Ayam Bawang",     # 5
        "Indomie Goreng Aceh",          # 6
        "Indomie Hype Abis Ayam Geprek",# 7
        "Indomie Salted Egg",           # 8
        "Indomie Goreng Jumbo",         # 9
        "Indomie Mi Goreng Iga Penyet"  # 10
    ]
    
    weights = [85, 91, 85, 75, 70, 90, 85, 100, 120, 91]  # dalam gram
    values = [90, 95, 85, 80, 75, 92, 88, 98, 100, 93]    # nilai kepuasan
    capacity = 400  # kapasitas tas dalam gram
    
    # =========================================================================
    # EKSEKUSI PROGRAM
    # =========================================================================
    
    # Tampilkan header
    print_header()
    
    # Tampilkan data
    print_data(item_names, weights, values, capacity)
    
    # Jalankan algoritma Knapsack DP
    max_value, dp_table = knapsack_dp(weights, values, capacity, item_names)
    
    # Dapatkan item yang terpilih
    selected_items, total_weight = get_selected_items(
        dp_table, weights, values, capacity, item_names
    )
    
    # Tampilkan tabel DP
    print_dp_table(dp_table, weights, capacity, item_names)
    
    # Tampilkan hasil
    print_result(max_value, selected_items, total_weight, capacity)
    
    # Perbandingan dengan brute force
    compare_with_brute_force(len(item_names))
    
    print("\n" + "=" * 70)
    print("Program selesai dijalankan!")
    print("=" * 70)
    
    return max_value, selected_items, total_weight


if __name__ == "__main__":
    main()
