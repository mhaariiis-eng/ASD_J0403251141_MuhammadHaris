#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
#==============================================

# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)

from collections import deque

# Representasi graph dunia nyata menggunakan Adjacency List
# Setiap lokasi (node) menyimpan daftar lokasi yang bisa dicapai langsung
graph = {
    'Rumah'        : ['Sekolah', 'Toko'],  # Dari Rumah bisa langsung ke Sekolah atau Toko
    'Sekolah'      : ['Perpustakaan'],     # Dari Sekolah bisa langsung ke Perpustakaan
    'Toko'         : ['Pasar'],            # Dari Toko bisa langsung ke Pasar
    'Perpustakaan' : [],                   # Perpustakaan tidak terhubung ke mana-mana (node daun)
    'Pasar'        : []                    # Pasar tidak terhubung ke mana-mana (node daun)
}

# Struktur graph yang terbentuk:
#
#   Rumah
#   /   \
# Sekolah Toko
#   |       |
# Perpus  Pasar

# Fungsi BFS untuk menelusuri graph level per level
def bfs(graph, start):

    # Set untuk mencatat lokasi yang sudah dikunjungi agar tidak diproses dua kali
    visited = set()

    # Antrian dimulai dengan node awal (start) langsung dimasukkan saat inisialisasi
    queue = deque([start])

    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    # Proses terus selama masih ada lokasi di dalam antrian
    while queue:

        # Ambil lokasi paling depan dari antrian (FIFO)
        node = queue.popleft()

        # Tampilkan lokasi yang sedang dikunjungi
        print(node, end=" ")

        # Periksa semua lokasi tetangga dari lokasi saat ini
        for neighbor in graph[node]:

            # Hanya masukkan tetangga yang belum pernah dikunjungi
            if neighbor not in visited:
                visited.add(neighbor)    # Tandai agar tidak masuk antrian dua kali
                queue.append(neighbor)   # Tambahkan ke antrian untuk diproses nanti

# Menjalankan BFS mulai dari 'Rumah'
# Output: Rumah Sekolah Toko Perpustakaan Pasar
# (level 0: Rumah → level 1: Sekolah, Toko → level 2: Perpustakaan, Pasar)
print("BFS dari Rumah:")
bfs(graph, 'Rumah')
print()

#.....................................................................
# PERTANYAAN ANALISIS
#.....................................................................

# 1. Node mana yang dikunjungi pertama?
# JAWAB: Node yang dikunjungi pertama adalah 'Rumah' karena merupakan
#        starting point / node awal dari algoritma BFS. BFS selalu
#        mengunjungi node awal terlebih dahulu sebelum menjelajahi
#        tetangga-tetangganya.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# JAWAB: BFS cocok untuk mencari jalur terdekat (shortest path) karena:
#        a) BFS menggunakan prinsip FIFO (First In First Out) dengan queue
#        b) BFS menjelajahi graph level per level dari node awal
#        c) Node yang ditemukan lebih awal PASTI memiliki jumlah langkah
#           (edge) paling sedikit untuk mencapai node tersebut
#        d) BFS menjamin menemukan jalur terpendek sebelum mengeksplorasi
#           jalur yang lebih panjang
#
#        Contoh pada graph ini:
#        - Rumah → Sekolah      = 1 langkah (level 1)
#        - Rumah → Toko         = 1 langkah (level 1)
#        - Rumah → Perpustakaan = 2 langkah (level 2) via Sekolah
#        - Rumah → Pasar        = 2 langkah (level 2) via Toko

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# JAWAB: Urutan BFS akan berubah tergantung jenis perubahannya:
#
#        a) Urutan neighbor dibalik → urutan kunjungan berubah
#           Contoh: 'Rumah': ['Toko', 'Sekolah']
#           Output lama : Rumah Sekolah Toko Perpustakaan Pasar
#           Output baru : Rumah Toko Sekolah Pasar Perpustakaan
#
#        b) Node/edge baru ditambahkan → node baru ikut dikunjungi
#           Contoh: 'Pasar': ['Apotek'] → Apotek akan muncul di output
#
#        c) Node/edge dihapus → node yang terisolasi tidak akan dikunjungi
#           Contoh: edge Rumah→Toko dihapus → Toko dan Pasar tidak terjangkau
#
#        d) Mekanisme BFS (FIFO, level per level) tidak berubah,
#           hanya URUTAN dan JANGKAUAN kunjungannya yang terpengaruh