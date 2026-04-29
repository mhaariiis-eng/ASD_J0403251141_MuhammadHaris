#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
#==============================================

#==========================================================
# Materi 1:Implementasi Dasar Graph
#==========================================================

# Membuat graph menggunakan dictionary (Adjacency List)
# Setiap key = node, value = list node tetangga yang terhubung
graph = {
    'A': ['B', 'C'],  # Node A terhubung ke node B dan C
    'B': ['A', 'D'],  # Node B terhubung ke node A dan D
    'C': ['A', 'D'],  # Node C terhubung ke node A dan D
    'D': ['B', 'C']   # Node D terhubung ke node B dan C
}

# Melakukan iterasi (perulangan) pada setiap node di dalam graph
for node in graph:
    # Menampilkan node beserta daftar tetangganya
    # graph[node] mengambil value (list tetangga) dari key node tersebut
    print(node, "->", graph[node])

# Output yang dihasilkan:
# A -> ['B', 'C']
# B -> ['A', 'D']
# C -> ['A', 'D']
# D -> ['B', 'C']