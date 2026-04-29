#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
#==============================================

#=================================================
# Materi 3 : Implementasi DFS
#=================================================

# Mengimpor deque dari library collections bawaan Python
# Catatan: pada DFS rekursif ini deque sebenarnya tidak digunakan,
# karena DFS memanfaatkan call stack (tumpukan pemanggilan fungsi) secara otomatis
from collections import deque

# Representasi graph menggunakan Adjacency List (dictionary)
# Struktur graph yang terbentuk:
#         A
#        / \
#       B   C
#      / \ / \
#     D  E F  G
graph = {
    'A' : ['B','C'],  # A terhubung ke B dan C (level 1)
    'B' : ['D','E'],  # B terhubung ke D dan E (level 2)
    'C' : ['F','G'],  # C terhubung ke F dan G (level 2)
    'D' : [],         # D tidak punya tetangga (node daun)
    'E' : [],         # E tidak punya tetangga (node daun)
    'F' : [],         # F tidak punya tetangga (node daun)
    'G' : [],         # G tidak punya tetangga (node daun)
}


def dfs(graph, node, visited):
    # Fungsi untuk menelusuri graph menggunakan algoritma DFS
    # (Depth First Search = penelusuran mendalam ke satu cabang dulu
    #  sebelum berpindah ke cabang berikutnya)
    # Parameter:
    #   graph   : dictionary yang menyimpan struktur graph
    #   node    : node yang sedang dikunjungi saat ini
    #   visited : set yang menyimpan node yang sudah dikunjungi

    # Menandai node saat ini sebagai sudah dikunjungi
    # agar tidak diproses ulang jika ditemukan lagi dari jalur lain
    visited.add(node)

    # Menampilkan node yang sedang dikunjungi saat ini
    print(node, end=" ")

    # Memeriksa semua tetangga langsung dari node saat ini
    for neighbor in graph[node]:

        # Hanya proses tetangga yang BELUM pernah dikunjungi
        if neighbor not in visited:

            # Memanggil fungsi dfs() secara rekursif pada tetangga tersebut
            # Artinya: sebelum lanjut ke tetangga berikutnya,
            # telusuri dulu seluruh cabang dari tetangga ini sampai habis
            dfs(graph, neighbor, visited)

# Membuat set kosong untuk mencatat node yang sudah dikunjungi
# Set dipakai karena pengecekan "in" lebih cepat O(1) dibanding list O(n)
visited = set()

# Menjalankan DFS mulai dari node 'A'
# Output yang dihasilkan: A B D E C F G
# (telusuri A → masuk ke B → masuk ke D (buntu) → balik ke B → masuk ke E (buntu)
#  → balik ke A → masuk ke C → masuk ke F (buntu) → balik ke C → masuk ke G (buntu))
dfs(graph, "A", visited)