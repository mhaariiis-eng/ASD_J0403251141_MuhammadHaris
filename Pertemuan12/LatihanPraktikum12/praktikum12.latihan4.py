#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Modul bawaan Python untuk operasi min-heap (priority queue)

# Graph lokasi kampus direpresentasikan sebagai dictionary bersarang.
# Setiap key adalah nama lokasi, dan value-nya adalah dictionary
# yang memetakan lokasi tujuan ke waktu tempuh dalam satuan menit.
# 'Aula' tidak memiliki edge keluar karena merupakan simpul tujuan akhir.
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga karena belum ada
    # jalur yang ditemukan ke lokasi manapun selain titik awal.
    distances = {node: float('inf') for node in graph}

    # Waktu tempuh dari titik awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue diisi dengan titik awal dan jarak 0.
    # Format setiap elemen: (jarak_terakumulasi, nama_lokasi).
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil lokasi dengan waktu tempuh terakumulasi terkecil.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika entry ini sudah usang — ada jalur lebih baik
        # yang ditemukan setelah entry ini dimasukkan ke antrian.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua lokasi yang dapat dicapai dari lokasi saat ini.
        for neighbor, weight in graph[current_node].items():
            # Hitung total waktu tempuh jika melewati lokasi saat ini.
            distance = current_distance + weight

            # Jika jalur ini lebih cepat dari yang sudah tercatat,
            # perbarui jarak dan masukkan ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Kembalikan dictionary berisi waktu tempuh terpendek ke semua lokasi.
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ============================================================
# Jawaban Analisis
# ============================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi terdekat adalah Kantin, dengan waktu tempuh 2 menit.
#    Kantin terhubung langsung ke Gerbang melalui edge berbobot 2,
#    yang merupakan nilai paling kecil dibanding semua lokasi lainnya.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendeknya adalah 7 menit.
#    Rute yang diambil: Gerbang → Kantin → Lab → Aula.
#    Rincian: Gerbang→Kantin (2) + Kantin→Lab (4) + Lab→Aula (1) = 7 menit.
#    Sebagai perbandingan, rute Gerbang→Kantin→Aula membutuhkan 2+7 = 9 menit,
#    dan Gerbang→Perpustakaan→Lab→Aula membutuhkan 6+3+1 = 10 menit.
#    Rute via Kantin→Lab terbukti paling efisien.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Dua contoh dari kasus ini membuktikannya:
#    - Gerbang ke Lab: tidak ada edge langsung, sehingga harus melewati
#      simpul perantara. Jalur terpendeknya Gerbang→Kantin→Lab = 2+4 = 6 menit.
#    - Gerbang ke Aula: rute "lebih langsung" Gerbang→Kantin→Aula = 9 menit,
#      tetapi rute dengan satu langkah tambahan Gerbang→Kantin→Lab→Aula
#      hanya 7 menit — lebih cepat meski melewati lebih banyak simpul.
#    Ini membuktikan bahwa jalur dengan lebih banyak langkah bisa lebih
#    singkat jika bobot tiap edge-nya kecil. Dijkstra dirancang untuk
#    menemukan jalur semacam ini secara otomatis.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Ada beberapa alasan yang menjadikan Dijkstra pilihan tepat di sini:
#
#    - Semua bobot bernilai positif: waktu tempuh antar lokasi tidak mungkin
#      bernilai negatif, sehingga syarat utama Dijkstra terpenuhi sepenuhnya.
#
#    - Graph kecil dan statis: jumlah lokasi kampus terbatas dan tidak
#      berubah-ubah, sehingga performa Dijkstra dapat dimanfaatkan secara optimal.
#
#    - Satu titik sumber: yang dibutuhkan hanya perhitungan dari satu titik
#      awal (Gerbang) ke semua lokasi lain — persis masalah Single Source
#      Shortest Path yang menjadi keunggulan Dijkstra.
#
#    - Lebih efisien dari Bellman-Ford: tanpa bobot negatif, tidak ada alasan
#      menggunakan Bellman-Ford yang lebih lambat. Dijkstra menyelesaikan
#      masalah ini lebih cepat berkat penggunaan priority queue.