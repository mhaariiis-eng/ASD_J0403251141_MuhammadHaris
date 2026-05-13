# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# Tujuan: Memahami cara kerja algoritma Prim dalam membentuk
#         MST secara bertahap mulai dari satu node awal,
#         dengan menggunakan priority queue (heap).
# ==========================================================

import heapq  # modul heap untuk priority queue (min-heap)

# Representasi graph dalam bentuk adjacency dict (kamus ketetanggaan)
# Format: {node: {tetangga: bobot, ...}}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    """
    Fungsi untuk mencari MST menggunakan algoritma Prim.
    Parameter:
        graph (dict): representasi weighted graph
        start (str) : node awal tempat MST dimulai
    Return:
        mst (list)        : daftar edge MST dalam format (u, v, bobot)
        total_weight (int): total bobot MST
    """

    # Langkah 1: Tandai node awal sebagai sudah dikunjungi
    visited = set([start])

    # Masukkan semua edge dari node awal ke priority queue
    # Format heap: (bobot, node_asal, node_tujuan)
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # menyimpan edge-edge terpilih
    total_weight = 0  # akumulasi total bobot

    print(f"\nMulai dari node awal: '{start}'")
    print("-" * 50)

    # Langkah 2-4: Proses sampai semua node terhubung
    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        # Langkah 2: Cek apakah node tujuan (v) belum dikunjungi
        if v not in visited:
            # Langkah 3: Tambahkan node v ke MST
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Pilih edge {u}-{v} (bobot {weight}) → Node aktif: {sorted(visited)}")

            # Tambahkan semua edge dari node v yang baru ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            # Edge ini dilewati karena node tujuan sudah dikunjungi
            print(f"  Lewati edge {u}-{v} (bobot {weight}) → '{v}' sudah dikunjungi")

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
print("=" * 50)
print("Algoritma Prim - Minimum Spanning Tree")
print("=" * 50)

mst, total = prim(graph, 'A')

# Tampilkan hasil MST
print("\n" + "=" * 50)
print("Hasil Minimum Spanning Tree (Prim):")
print("=" * 50)
for u, v, w in mst:
    print(f"  {u} -- {v}  (bobot: {w})")
print(f"\nTotal bobot MST = {total}")
print("=" * 50)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'. Node awal dapat dipilih
#    bebas; hasilnya (total bobot MST) akan tetap sama meskipun
#    node awal berbeda, karena MST bersifat unik pada graph ini.

# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2 dipilih pertama, karena dari node A,
#    edge terkecil yang tersedia adalah A-C (bobot 2), lebih kecil
#    dari A-B (4) dan A-D (5).

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan min-heap (priority queue) yang selalu
#    menyimpan semua edge yang menghubungkan node-sudah-dikunjungi
#    dengan node-belum-dikunjungi. Setiap kali, diambil edge
#    dengan bobot terkecil dari heap. Jika node tujuan belum
#    dikunjungi, edge diterima dan node baru ditambahkan ke tree.
#    Proses berlanjut hingga semua node masuk ke dalam tree.

# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST = 2 + 1 + 3 = 6
#    (dari edge A-C=2, C-D=1, D-B=3)

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Kruskal: bekerja GLOBAL → mengurutkan semua edge dulu,
#      lalu memilih edge terkecil yang tidak membentuk cycle.
#      Cocok untuk sparse graph (sedikit edge).
#    - Prim: bekerja LOKAL → mulai dari satu node, lalu meluas
#      ke tetangga terdekat yang belum terhubung. Cocok untuk
#      dense graph (banyak edge).
#    Keduanya menghasilkan MST dengan total bobot yang sama.
