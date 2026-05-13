# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Materi 1 - Algoritma Kruskal
# Tujuan: Memahami dan mengimplementasikan algoritma Kruskal
#         untuk mencari Minimum Spanning Tree (MST) pada
#         weighted graph dengan memilih edge berbobot terkecil
#         secara global dan menghindari pembentukan cycle.
# ==========================================================

# ----------------------------------------------------------
# Konsep Kruskal:
# - Bekerja secara GLOBAL: mengurutkan semua edge dulu
# - Setiap edge dipilih dari yang terkecil
# - Edge ditolak jika akan membentuk cycle
# - Cocok untuk sparse graph (sedikit edge)
# ----------------------------------------------------------

# Daftar edge graph: format (bobot, node1, node2)
# Graph: A-B=4, A-C=2, A-D=5, B-D=3, C-D=1
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Langkah 1: Urutkan semua edge berdasarkan bobot terkecil
# Python sort pada tuple membandingkan elemen pertama (bobot) terlebih dahulu
edges.sort()

# Inisialisasi MST dan variabel bantu
mst = []           # menyimpan edge-edge yang masuk MST
total_weight = 0   # akumulasi total bobot MST

# Set sederhana untuk melacak node yang sudah terhubung ke MST
# Pendekatan: edge diterima jika salah satu node-nya belum ada di set
connected = set()

# Langkah 2-6: Iterasi setiap edge dari yang terkecil
for weight, u, v in edges:
    # Langkah 3: Periksa apakah edge akan membentuk cycle
    # Edge aman jika minimal satu node belum masuk ke 'connected'
    if u not in connected or v not in connected:
        # Langkah 4: Tidak membentuk cycle → tambahkan ke MST
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Tampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# ----------------------------------------------------------
# Catatan tentang keterbatasan implementasi sederhana ini:
# Pengecekan cycle dengan set() di atas hanya bekerja dengan
# benar untuk kasus sederhana. Untuk graph yang lebih kompleks,
# diperlukan struktur data Union-Find (Disjoint Set) agar
# pendeteksian cycle lebih akurat dan efisien.
#
# Kelemahan Kruskal secara umum:
# - Memerlukan pengurutan semua edge di awal → O(E log E)
# - Kurang efisien pada dense graph (banyak edge)
# - Deteksi cycle bisa kompleks tanpa Union-Find
# ----------------------------------------------------------