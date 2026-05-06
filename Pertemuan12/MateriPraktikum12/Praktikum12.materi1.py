#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
#Materi 1: Algoritma Dijkstra untuk Shortest Path
#==============================================

# Modul heapq digunakan untuk mengoperasikan min-heap sebagai priority queue,
# yaitu struktur data yang selalu menempatkan elemen terkecil di posisi teratas.
import heapq

# Weighted graph yang direpresentasikan sebagai dictionary bersarang.
# Setiap key adalah nama simpul, dan value-nya adalah dictionary
# yang memetakan tetangga ke bobot (jarak) masing-masing edge.
# Simpul 'D' tidak memiliki edge keluar sehingga value-nya dictionary kosong.
graph = {
    'A': {'B': 4, 'C': 2},   # A terhubung ke B (jarak 4) dan C (jarak 2)
    'B': {'D': 5},            # B terhubung ke D (jarak 5)
    'C': {'D': 1},            # C terhubung ke D (jarak 1)
    'D': {}                   # D tidak memiliki tetangga (simpul tujuan akhir)
}


def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga karena belum ada jalur
    # yang ditemukan ke simpul manapun selain simpul awal.
    distances = {node: float('inf') for node in graph}

    # Jarak dari simpul awal ke dirinya sendiri selalu 0.
    distances[start] = 0

    # Priority queue diisi dengan simpul awal dan jarak 0.
    # Format setiap elemen: (jarak_terakumulasi, nama_simpul).
    # Dijkstra selalu memproses simpul dengan jarak terkecil lebih dahulu.
    pq = [(0, start)]

    # Terus proses selama masih ada simpul di dalam antrian.
    while pq:
        # Ambil simpul dengan jarak terakumulasi terkecil dari antrian.
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga yang dapat dijangkau dari simpul saat ini.
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak jika jalur melewati simpul saat ini menuju tetangga.
            distance = current_distance + weight

            # Jika jalur baru ini lebih pendek dari jarak terbaik yang tersimpan,
            # perbarui jarak tetangga dan masukkan ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Kembalikan dictionary berisi jarak terpendek ke seluruh simpul.
    return distances

hasil = dijkstra(graph, 'A')
print(hasil)