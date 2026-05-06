#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph yang memuat bobot negatif.
# 'A' terhubung ke 'B' (bobot 5) dan 'C' (bobot 4).
# 'C' terhubung ke 'B' dengan bobot negatif -2.
# 'B' tidak memiliki edge keluar.
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Mencari jarak terpendek dari simpul awal (start) ke semua simpul lain
    menggunakan algoritma Bellman-Ford, yang mendukung bobot edge negatif.
    """
    # Inisialisasi semua jarak dengan tak hingga karena belum ada jalur
    # yang ditemukan ke simpul manapun selain simpul awal.
    distances = {node: float('inf') for node in graph}

    # Jarak dari simpul awal ke dirinya sendiri selalu 0.
    distances[start] = 0

    # Lakukan relaksasi sebanyak (jumlah simpul - 1) kali.
    # Jumlah iterasi ini menjamin semua jalur terpendek ditemukan
    # selama tidak ada siklus negatif dalam graph.
    for _ in range(len(graph) - 1):
        # Periksa setiap edge dalam graph pada setiap iterasi.
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Relaksasi: jika simpul saat ini sudah dapat dijangkau
                # dan jalur melewatinya menghasilkan jarak lebih kecil
                # ke tetangga, perbarui jarak tetangga tersebut.
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Kembalikan dictionary berisi jarak terpendek ke seluruh simpul.
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ============================================================
# Jawaban Analisis
# ============================================================

# 1. Berapa bobot langsung dari A ke B?
#    Bobot edge langsung A → B adalah 5.
#    Hal ini terlihat dari definisi graph: 'A': {'B': 5, 'C': 4},
#    yang menyatakan edge A→B memiliki bobot 5.

# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobotnya adalah 2.
#    Perhitungan: bobot A→C (4) ditambah bobot C→B (-2) = 2.
#    Adanya bobot negatif pada edge C→B membuat jalur ini
#    lebih hemat dibanding rute langsung A→B yang berbobot 5.

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A → C → B lebih pendek dengan total bobot 2.
#    Rute langsung A → B bernilai 5, sedangkan A → C → B hanya
#    4 + (-2) = 2. Karena 2 < 5, algoritma menetapkan A → C → B
#    sebagai jalur terpendek, yang juga dikonfirmasi output: B = 2.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Bellman-Ford tidak langsung mengunci jarak suatu simpul setelah
#    pertama kali diproses. Sebaliknya, algoritma ini merelaksasi
#    semua edge secara berulang sebanyak (V-1) kali, memberi kesempatan
#    setiap simpul untuk terus memperbarui jaraknya jika ditemukan
#    jalur yang lebih pendek — termasuk yang melewati edge negatif.
#    Berbeda dengan Dijkstra yang bersifat "serakah" dan langsung
#    memfinalisasi jarak, Bellman-Ford bersedia merevisi jarak
#    yang sudah ada selama iterasi masih berlangsung.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah pemeriksaan apakah jarak ke suatu tetangga
#    bisa diperbarui menjadi lebih kecil melalui simpul yang sedang
#    diproses. Formulanya:
#        if distances[node] + weight < distances[neighbor]:
#            distances[neighbor] = distances[node] + weight
#    Maknanya: "Jika jarak ke simpul saat ini ditambah bobot edge-nya
#    lebih kecil dari jarak terbaik yang sudah diketahui ke tetangga,
#    maka perbarui jarak tetangga tersebut." Proses ini diulang untuk
#    semua edge di tiap iterasi, sehingga informasi jarak terpendek
#    menyebar secara bertahap ke seluruh simpul dalam graph.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#
#    - Dukungan bobot negatif:
#      Dijkstra tidak mendukung bobot negatif.
#      Bellman-Ford mendukung bobot negatif.
#
#    - Strategi pemrosesan:
#      Dijkstra selalu memproses simpul dengan jarak terkecil lebih dulu
#      (pendekatan greedy).
#      Bellman-Ford merelaksasi semua edge secara berulang sebanyak (V-1) kali.
#
#    - Struktur data utama:
#      Dijkstra mengandalkan priority queue (min-heap).
#      Bellman-Ford hanya menggunakan nested loop biasa.
#
#    - Kompleksitas waktu:
#      Dijkstra: O((V + E) log V) — lebih cepat dan efisien.
#      Bellman-Ford: O(V × E) — lebih lambat namun lebih fleksibel.
#
#    - Deteksi siklus negatif:
#      Dijkstra tidak mampu mendeteksi negative cycle.
#      Bellman-Ford dapat mendeteksinya pada iterasi ke-V.
#
#    Kesimpulan: Gunakan Dijkstra jika semua bobot bernilai positif dan
#    efisiensi waktu menjadi prioritas. Gunakan Bellman-Ford jika graph
#    mengandung bobot negatif atau perlu mendeteksi adanya siklus negatif.