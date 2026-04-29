#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
#==============================================

#=================================================
# Materi 2 : Implementasi BFS
#=================================================

# Mengimpor deque dari library collections bawaan Python
# deque (double-ended queue) dipakai sebagai antrian karena
# operasi popleft()-nya O(1), lebih efisien dibanding list biasa yang O(n)
from collections import deque

# Representasi graph menggunakan Adjacency List (dictionary)
# Setiap key = node, value = list node tetangga langsung
# Node D, E, F, G bernilai [] karena tidak punya anak (node daun / leaf)
graph = {
    'A' : ['B','C'],  # A terhubung ke B dan C (level 1)
    'B' : ['D','E'],  # B terhubung ke D dan E (level 2)
    'C' : ['F','G'],  # C terhubung ke F dan G (level 2)
    'D' : [],         # D tidak punya tetangga (node daun)
    'E' : [],         # E tidak punya tetangga (node daun)
    'F' : [],         # F tidak punya tetangga (node daun)
    'G' : [],         # G tidak punya tetangga (node daun)
}

# Struktur graph yang terbentuk:
#         A
#        / \
#       B   C
#      / \ / \
#     D  E F  G

def bfs(graph, start):
    # Fungsi untuk menelusuri graph menggunakan algoritma BFS
    # (Breadth First Search = penelusuran melebar per level)
    # Parameter:
    #   graph : dictionary yang menyimpan struktur graph
    #   start : node awal tempat penelusuran dimulai

    # Membuat antrian kosong menggunakan deque
    # Antrian ini menyimpan node yang sudah ditemukan tapi belum diproses
    queue = deque()

    # Membuat set kosong untuk mencatat node yang sudah dikunjungi
    # Set dipakai karena pengecekan "in" pada set lebih cepat (O(1)) dibanding list (O(n))
    visited = set()

    # Memasukkan node awal ke dalam antrian sebagai titik mulai
    queue.append(start)

    # Menandai node awal sebagai sudah dikunjungi agar tidak diproses ulang
    visited.add(start)

    # Looping terus selama antrian masih berisi node yang belum diproses
    while queue:

        # Mengambil dan menghapus node paling depan dari antrian (FIFO)
        # Inilah yang membuat BFS menelusuri node level per level
        node = queue.popleft()

        # Menampilkan node yang sedang dikunjungi saat ini
        print(node, end=" ")

        # Memeriksa semua tetangga langsung dari node yang sedang diproses
        for neighbor in graph[node]:

            # Hanya proses tetangga yang BELUM pernah dikunjungi
            # Ini mencegah node yang sama dikunjungi lebih dari sekali
            if neighbor not in visited:

                # Tandai tetangga sebagai sudah dikunjungi sebelum dimasukkan ke antrian
                # Ditandai di sini (bukan saat diambil) agar tidak masuk antrian dua kali
                visited.add(neighbor)

                # Masukkan tetangga ke bagian belakang antrian
                # untuk diproses setelah semua node di level saat ini selesai
                queue.append(neighbor)

# Menjalankan BFS mulai dari node 'A'
# Output yang dihasilkan: A B C D E F G
# (ditelusuri level per level dari atas ke bawah)
bfs(graph, 'A')