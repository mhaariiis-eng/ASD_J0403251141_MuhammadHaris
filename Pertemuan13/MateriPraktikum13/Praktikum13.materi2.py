# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Materi 2 - Algoritma Prim
# Tujuan: Memahami dan mengimplementasikan algoritma Prim
#         untuk mencari Minimum Spanning Tree (MST) dengan
#         cara membangun tree secara bertahap mulai dari
#         satu node awal menggunakan priority queue (heap).
# ==========================================================

import heapq  # modul bawaan Python untuk min-heap (priority queue)

# ----------------------------------------------------------
# Konsep Prim:
# - Bekerja secara LOKAL: mulai dari satu node, lalu meluas
# - Setiap langkah: pilih edge terkecil ke node baru
# - Cycle otomatis dihindari karena hanya node baru yang dipilih
# - Cocok untuk dense graph (banyak edge)
# ----------------------------------------------------------

# Representasi graph dalam bentuk adjacency dict (kamus ketetanggaan)
# Format: {node: {tetangga: bobot, ...}}
# Graph: A-B=4, A-C=2, A-D=5, B-D=3, C-D=1
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    """
    Mencari MST menggunakan algoritma Prim.

    Parameter:
        graph (dict): weighted graph dalam bentuk adjacency dict
        start (str) : node awal tempat pembangunan MST dimulai

    Return:
        mst (list)         : daftar edge MST (node_asal, node_tujuan, bobot)
        total_weight (int) : total bobot seluruh edge MST
    """

    # Langkah 1: Tandai node awal sebagai sudah dikunjungi
    visited = set([start])

    # Priority queue berisi edge kandidat: (bobot, node_asal, node_tujuan)
    # heapq Python adalah min-heap → selalu pop elemen terkecil
    edges = []

    # Masukkan semua edge dari node awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []          # menyimpan edge-edge terpilih
    total_weight = 0  # akumulasi total bobot MST

    # Langkah 2-4: Proses terus sampai tidak ada edge kandidat
    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        # Langkah 2: Cek apakah node tujuan (v) belum dikunjungi
        if v not in visited:
            # Langkah 3: Node baru → tambahkan edge ke MST
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan semua edge dari node v yang baru ke heap
            # (hanya ke node yang belum dikunjungi)
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

        # Jika v sudah dikunjungi, edge ini dilewati (otomatis hindari cycle)

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ----------------------------------------------------------
# Perbandingan Kruskal (Materi 1) vs Prim (Materi 2):
#
# Aspek         | Kruskal               | Prim
# --------------|------------------------|------------------------
# Pendekatan    | Edge global terkecil  | Meluas dari node awal
# Fokus         | Edge                  | Node
# Cocok untuk   | Sparse graph          | Dense graph
# Deteksi cycle | Perlu Union-Find      | Otomatis (visited set)
# Struktur data | Sorted list           | Min-heap (heapq)
#
# Keduanya menghasilkan MST dengan total bobot yang sama.
# ----------------------------------------------------------