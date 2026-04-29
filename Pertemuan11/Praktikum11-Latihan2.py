#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
#==============================================

# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)

# Representasi graph menggunakan Adjacency List
# Struktur graph yang terbentuk:
#
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
graph = {
    'A': ['B', 'C'],  # A terhubung ke B dan C (level 1)
    'B': ['D', 'E'],  # B terhubung ke D dan E (level 2)
    'C': ['F'],       # C hanya terhubung ke F (level 2)
    'D': [],          # D tidak punya tetangga (node daun)
    'E': [],          # E tidak punya tetangga (node daun)
    'F': []           # F tidak punya tetangga (node daun)
}

# Fungsi DFS rekursif untuk menelusuri graph secara mendalam
def dfs(graph, node, visited):

    # Tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        # Hanya proses tetangga yang belum dikunjungi
        if neighbor not in visited:

            # Panggil DFS secara rekursif → telusuri cabang ini
            # sampai ke node terdalam (daun) sebelum kembali (backtrack)
            dfs(graph, neighbor, visited)

# Membuat set kosong untuk mencatat node yang sudah dikunjungi
visited = set()

# Menjalankan DFS mulai dari node 'A'
# Alur penelusuran:
# A → masuk B → masuk D (daun, backtrack) → masuk E (daun, backtrack)
# → backtrack ke A → masuk C → masuk F (daun, backtrack) → selesai
# Output: A B D E C F
print("DFS dari A:")
dfs(graph, 'A', visited)
print()

#.....................................................................
# PERTANYAAN ANALISIS
#.....................................................................

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# JAWAB: DFS menggunakan prinsip rekursi yang bekerja seperti stack LIFO
#        (Last In First Out):
#        a) Setiap kali DFS menemukan tetangga yang belum dikunjungi,
#           ia langsung memanggil dirinya sendiri (rekursif) tanpa
#           menunggu tetangga lain selesai diproses
#        b) Pemanggilan rekursif membentuk call stack → node yang paling
#           baru dipanggil diproses lebih dulu (LIFO)
#        c) DFS terus "menggali ke dalam" satu cabang sampai mencapai
#           node daun (tidak punya tetangga), baru kemudian backtrack
#           ke persimpangan sebelumnya dan mencoba cabang berikutnya
#
#        Contoh alur pada graph ini:
#        A → B → D (daun, backtrack) → E (daun, backtrack) → C → F (daun)

# 2. Apa yang terjadi jika urutan neighbor diubah?
# JAWAB: Urutan neighbor di adjacency list menentukan cabang mana yang
#        dijelajahi lebih dulu oleh DFS:
#        a) DFS selalu mengikuti tetangga pertama yang ditemukan di list
#        b) Jika 'A': ['B', 'C'] diubah menjadi 'A': ['C', 'B']:
#           - Output lama : A B D E C F  (cabang B dulu)
#           - Output baru : A C F B D E  (cabang C dulu)
#        c) Semua node tetap akan dikunjungi selama masih terhubung,
#           hanya URUTAN kunjungannya yang berubah
#        d) Sifat DFS (selalu masuk ke cabang terdalam dulu) tidak berubah

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama
# JAWAB:
#        DFS dari A : A B D E C F  → masuk sedalam mungkin per cabang
#        BFS dari A : A B C D E F  → jelajahi semua node level per level
#
#        Perbandingan detail:
#
#        a) CARA EKSPLORASI:
#           - DFS : Satu cabang diselesaikan sampai daun, baru cabang lain
#           - BFS : Semua node di level yang sama dikunjungi sebelum turun
#
#        b) STRUKTUR DATA:
#           - DFS : Stack implisit dari rekursi (LIFO)
#           - BFS : Queue / antrian eksplisit (FIFO)
#
#        c) KEGUNAAN:
#           - DFS : Cocok untuk deteksi siklus, topological sort,
#                   dan eksplorasi semua kemungkinan jalur
#           - BFS : Cocok untuk mencari jalur terpendek (shortest path)
#                   dan penelusuran level per level
#
#        d) KOMPLEKSITAS WAKTU & RUANG:
#           - Keduanya O(V + E), V = jumlah node, E = jumlah edge
#           - Perbedaannya hanya pada STRATEGI dan URUTAN penelusuran