# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 5 - Tugas Mandiri: MST dengan Kasus Baru
# Kasus yang dipilih: Kasus 2 - Jaringan Komputer (Router)
# Tujuan: Menentukan koneksi antar router dengan total biaya
#         minimum menggunakan algoritma Kruskal dengan
#         Union-Find (Disjoint Set) yang benar.
# ==========================================================

# ----------------------------------------------------------
# Data koneksi antar router (weighted graph):
# RouterA - RouterB = 3
# RouterA - RouterC = 2
# RouterB - RouterD = 5
# RouterC - RouterD = 1
# RouterB - RouterC = 4
# ----------------------------------------------------------

# Representasi graph sebagai adjacency dict (untuk visualisasi)
graph_info = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# Daftar edge untuk algoritma Kruskal: (bobot, node1, node2)
edges = [
    (1, 'RouterC', 'RouterD'),
    (2, 'RouterA', 'RouterC'),
    (3, 'RouterA', 'RouterB'),
    (4, 'RouterB', 'RouterC'),
    (5, 'RouterB', 'RouterD')
]

# ----------------------------------------------------------
# Implementasi Union-Find (Disjoint Set)
# Digunakan oleh Kruskal untuk mendeteksi cycle secara akurat
# ----------------------------------------------------------

class UnionFind:
    """
    Struktur data Union-Find untuk mendeteksi cycle pada graph.
    - find(x)     : mencari root/representatif dari node x
    - union(x, y) : menggabungkan dua komponen yang berbeda
    """

    def __init__(self, nodes):
        # Setiap node awalnya menjadi representatif dirinya sendiri
        self.parent = {node: node for node in nodes}
        self.rank   = {node: 0 for node in nodes}

    def find(self, x):
        # Path compression: langsung hubungkan ke root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Gabungkan dua set. Return True jika berhasil (tidak cycle),
        Return False jika x dan y sudah satu komponen (cycle).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # sudah terhubung → akan membentuk cycle

        # Union by rank: pohon lebih pendek digabung ke pohon lebih tinggi
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True  # berhasil digabung


# ----------------------------------------------------------
# Algoritma Kruskal dengan Union-Find
# ----------------------------------------------------------

def kruskal(edges, nodes):
    """
    Mencari MST menggunakan algoritma Kruskal.
    Parameter:
        edges (list): daftar edge (bobot, u, v)
        nodes (list): daftar semua node
    Return:
        mst (list)         : edge-edge terpilih (u, v, bobot)
        total_weight (int) : total bobot MST
    """
    # Langkah 1: Urutkan semua edge berdasarkan bobot terkecil
    sorted_edges = sorted(edges)

    # Inisialisasi Union-Find untuk semua node
    uf = UnionFind(nodes)

    mst = []
    total_weight = 0

    print("\nProses pemilihan edge (Kruskal):")
    print("-" * 55)

    for weight, u, v in sorted_edges:
        # Langkah 3-5: Cek cycle dengan Union-Find
        if uf.union(u, v):
            # Tidak membentuk cycle → tambahkan ke MST
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Pilih {u} - {v}  (bobot {weight})  → DITERIMA ✓")
        else:
            # Membentuk cycle → abaikan
            print(f"  Pilih {u} - {v}  (bobot {weight})  → DITOLAK (cycle) ✗")

        # Berhenti jika sudah N-1 edge terpilih
        if len(mst) == len(nodes) - 1:
            break

    return mst, total_weight


# Kumpulkan semua node dari graph
all_nodes = list(graph_info.keys())

# Tampilkan header dan info graph
print("=" * 55)
print("Kasus 2: Jaringan Komputer - Koneksi Antar Router")
print("=" * 55)
print("\nDaftar semua koneksi yang tersedia:")
print(f"  {'Koneksi':<30} {'Biaya'}")
print("  " + "-" * 38)
ditampilkan = set()
for r, tetangga in graph_info.items():
    for tujuan, biaya in tetangga.items():
        pasangan = tuple(sorted([r, tujuan]))
        if pasangan not in ditampilkan:
            print(f"  {r} ↔ {tujuan:<20} {biaya}")
            ditampilkan.add(pasangan)

# Jalankan algoritma Kruskal
mst, total = kruskal(edges, all_nodes)

# Tampilkan hasil MST
print("\n" + "=" * 55)
print("Hasil MST - Jaringan Router dengan Biaya Minimum:")
print("=" * 55)
print(f"\n  {'Koneksi':<35} {'Biaya'}")
print("  " + "-" * 43)
for u, v, w in mst:
    print(f"  {u} ↔ {v:<22} {w}")
print("  " + "-" * 43)
print(f"  {'TOTAL BIAYA MINIMUM':<35} {total}")
print("=" * 55)
print(f"\nJumlah router       : {len(all_nodes)}")
print(f"Jumlah koneksi MST  : {len(mst)} (= {len(all_nodes)} router - 1)")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer - menentukan koneksi antar
#    router (RouterA, RouterB, RouterC, RouterD) dengan biaya
#    koneksi minimum.

# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal dengan struktur data Union-Find (Disjoint Set).
#    Union-Find digunakan untuk mendeteksi cycle secara efisien
#    dengan kompleksitas hampir O(1) per operasi (amortized).

# 3. Edge mana saja yang dipilih dalam MST?
#    - RouterC ↔ RouterD  (bobot 1)
#    - RouterA ↔ RouterC  (bobot 2)
#    - RouterA ↔ RouterB  (bobot 3)
#    Ketiga edge ini menghubungkan 4 router dengan 3 koneksi (N-1).

# 4. Berapa total bobot MST?
#    Total bobot = 1 + 2 + 3 = 6

# 5. Mengapa edge tertentu tidak dipilih?
#    - RouterB ↔ RouterC (bobot 4): tidak dipilih karena saat
#      diproses, RouterB dan RouterC sudah berada dalam satu
#      komponen yang sama (sudah terhubung via RouterA-RouterC).
#      Menambahkan edge ini akan membentuk cycle: RouterA-RouterC-RouterB-RouterA.
#    - RouterB ↔ RouterD (bobot 5): tidak dipilih karena semua
#      4 router sudah terhubung setelah 3 edge pertama dipilih.
#      Selain itu juga akan membentuk cycle.
