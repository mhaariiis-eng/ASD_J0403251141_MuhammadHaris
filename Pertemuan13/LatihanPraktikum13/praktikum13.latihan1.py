# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 1 - Memahami Konsep Spanning  Tree
# Tujuan: Menampilkan daftar edge graph, contoh spanning tree
#         yang valid, jumlah edge graph awal, dan jumlah edge
#         pada spanning tree.
# ==========================================================

# Daftar edge graph awal (semua koneksi yang ada)
# Graph terdiri dari 4 node: A, B, C, D
# dengan 5 edge yang mencakup berbagai koneksi termasuk cycle
edges = [
    ('A', 'B'),  # koneksi A ke B
    ('A', 'C'),  # koneksi A ke C
    ('A', 'D'),  # koneksi A ke D (membentuk cycle bersama C-D)
    ('C', 'D'),  # koneksi C ke D
    ('B', 'D')   # koneksi B ke D
]

# Contoh spanning tree yang valid dari graph di atas
# Spanning tree: A-C, C-D, D-B
# - Semua 4 node (A, B, C, D) terhubung
# - Tidak ada cycle
# - Jumlah edge = jumlah node - 1 = 4 - 1 = 3
spanning_tree = [
    ('A', 'C'),  # edge 1: menghubungkan A dan C
    ('C', 'D'),  # edge 2: menghubungkan C dan D
    ('D', 'B')   # edge 3: menghubungkan D dan B
]

# Tampilkan daftar edge pada graph awal
print("=" * 40)
print("Edge pada graph awal:")
print("=" * 40)
for edge in edges:
    print(f"  {edge[0]} -- {edge[1]}")

# Tampilkan contoh spanning tree yang valid
print("\n" + "=" * 40)
print("Contoh Spanning Tree yang Valid:")
print("=" * 40)
for edge in spanning_tree:
    print(f"  {edge[0]} -- {edge[1]}")

# Tampilkan jumlah edge pada graph awal dan spanning tree
print("\n" + "=" * 40)
print(f"Jumlah edge graph awal    = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")
print("=" * 40)

# Verifikasi bahwa spanning tree menghubungkan semua node
all_nodes_graph = set()
for u, v in edges:
    all_nodes_graph.add(u)
    all_nodes_graph.add(v)

nodes_in_st = set()
for u, v in spanning_tree:
    nodes_in_st.add(u)
    nodes_in_st.add(v)

print(f"\nNode pada graph       : {sorted(all_nodes_graph)}")
print(f"Node pada spanning tree: {sorted(nodes_in_st)}")
print(f"Semua node terhubung  : {all_nodes_graph == nodes_in_st}")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle (contoh:
#    A-C-D-A dan A-B-D-A), sedangkan spanning tree hanya memiliki
#    3 edge (= jumlah node - 1 = 4 - 1), menghubungkan seluruh
#    node tanpa membentuk cycle sama sekali.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur alternatif yang berlebihan untuk
#    mencapai node yang sama. Ini menyebabkan pemborosan edge
#    dan meningkatkan biaya total. Dalam konteks jaringan nyata
#    (kabel, jalan, dll.), edge berlebih = biaya sia-sia karena
#    koneksi sudah tercapai lewat jalur lain.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk menghubungkan N node tanpa cycle, dibutuhkan tepat
#    N-1 edge. Jika lebih dari N-1, pasti ada cycle. Jika kurang,
#    ada node yang tidak terhubung. Pada contoh ini: 4 node
#    membutuhkan tepat 3 edge, sedangkan graph awal punya 5 edge
#    (2 edge berlebih yang membentuk cycle).
