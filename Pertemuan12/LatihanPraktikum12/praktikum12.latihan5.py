#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# 1. Representasi weighted graph menggunakan dictionary bersarang.
#    Setiap key adalah nama kota, dan value-nya adalah dictionary
#    yang memetakan kota tetangga ke bobot (jarak) edge-nya.
#    'Bandung' tidak memiliki edge keluar karena merupakan simpul tujuan akhir.
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari simpul 'start' ke semua simpul lain
    dalam weighted graph menggunakan algoritma Dijkstra.

    Parameter:
        graph (dict) : weighted graph dalam format adjacency dictionary
        start (str)  : nama simpul yang dijadikan titik awal

    Return:
        distances (dict) : jarak terpendek dari start ke setiap simpul
    """
    # Inisialisasi semua jarak dengan tak hingga karena belum ada jalur
    # yang ditemukan ke simpul manapun selain simpul awal.
    distances = {node: float('inf') for node in graph}

    # Jarak dari simpul awal ke dirinya sendiri selalu 0.
    distances[start] = 0

    # Priority queue diisi dengan simpul awal dan jarak 0.
    # Format setiap elemen: (jarak_terakumulasi, nama_simpul).
    # heapq otomatis menempatkan elemen dengan jarak terkecil di posisi teratas.
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil simpul dengan jarak terakumulasi terkecil dari antrian.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati entry ini jika sudah usang — artinya ada jalur lebih pendek
        # ke simpul ini yang sudah ditemukan dan dimasukkan ke antrian sebelumnya.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota yang dapat dicapai dari simpul saat ini.
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak jika jalur melewati simpul saat ini menuju tetangga.
            distance = current_distance + weight

            # Relaksasi: jika jalur baru lebih pendek dari yang sudah tercatat,
            # perbarui jarak dan masukkan tetangga ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Kembalikan dictionary berisi jarak terpendek ke seluruh simpul.
    return distances

# 3. Tentukan simpul awal pencarian jalur terpendek.
node_awal = 'Bogor'

# 4. Jalankan Dijkstra dan tampilkan hasil jarak terpendek ke setiap kota.
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")


# ============================================================
# Jawaban Analisis
# ============================================================

# 1. Node awal yang digunakan apa?
#    Simpul awal yang digunakan adalah Bogor.
#    Ditetapkan melalui variabel: node_awal = 'Bogor'.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Simpul dengan jarak terkecil (selain Bogor sendiri) adalah Depok = 2.
#    Depok terhubung langsung ke Bogor dengan bobot edge paling kecil, yaitu 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Simpul dengan jarak terbesar adalah Bandung = 8.
#    Rute terpendek ke Bandung: Bogor → Depok → Bandung = 2 + 6 = 8.
#    Rute alternatif Bogor → Jakarta → Bandung = 5 + 7 = 12, lebih jauh.
#    Rute alternatif Bogor → Depok → Jakarta → Bandung = 2 + 2 + 7 = 11, juga lebih jauh.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini.
#
#    Kondisi awal:
#    - Semua jarak diinisialisasi tak hingga, kecuali Bogor = 0.
#    - Priority queue dimulai dengan: [(0, 'Bogor')].
#
#    Iterasi 1 — proses Bogor (jarak 0):
#    - Periksa tetangga: Jakarta (0+5=5) dan Depok (0+2=2).
#    - Perbarui distances: Jakarta=5, Depok=2.
#    - Priority queue: [(2, 'Depok'), (5, 'Jakarta')].
#
#    Iterasi 2 — proses Depok (jarak 2, terkecil di antrian):
#    - Periksa tetangga: Jakarta (2+2=4) dan Bandung (2+6=8).
#    - Jakarta diperbarui dari 5 menjadi 4 karena 4 < 5.
#    - Bandung diperbarui dari tak hingga menjadi 8.
#    - Priority queue: [(4, 'Jakarta'), (5, 'Jakarta'), (8, 'Bandung')].
#
#    Iterasi 3 — proses Jakarta (jarak 4, terkecil di antrian):
#    - Periksa tetangga: Bandung (4+7=11).
#    - 11 > 8 (jarak Bandung saat ini), sehingga tidak diperbarui.
#    - Priority queue: [(5, 'Jakarta'), (8, 'Bandung')].
#
#    Iterasi 4 — proses Jakarta (jarak 5, dilewati):
#    - 5 > distances['Jakarta'] yang sudah bernilai 4, entry ini dilewati.
#
#    Iterasi 5 — proses Bandung (jarak 8):
#    - Bandung tidak memiliki tetangga, tidak ada relaksasi yang dilakukan.
#    - Priority queue kosong, algoritma selesai.