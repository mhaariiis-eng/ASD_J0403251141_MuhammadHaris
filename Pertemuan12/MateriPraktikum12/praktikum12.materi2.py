#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
#Materi 2: Algoritma Bellman-Ford untuk Shortest Path
#==============================================

# Fungsi untuk mencari jarak terpendek dari satu simpul awal ke semua simpul lain
# menggunakan algoritma Bellman-Ford, yang mendukung edge berbobot negatif.
# Parameter:
#   graph — weighted graph dalam format dictionary bersarang
#   start — nama simpul yang dijadikan titik awal pencarian
def bellman_ford(graph, start):

    # Inisialisasi semua jarak dengan tak hingga karena belum ada jalur
    # yang ditemukan ke simpul manapun selain simpul awal.
    distances = {node: float('inf') for node in graph}

    # Jarak dari simpul awal ke dirinya sendiri selalu 0.
    distances[start] = 0

    # Lakukan relaksasi sebanyak (jumlah simpul - 1) kali.
    # Jumlah iterasi ini menjamin semua jarak terpendek sudah ditemukan
    # selama tidak ada siklus negatif di dalam graph.
    for _ in range(len(graph) - 1):

        # Periksa setiap simpul yang ada dalam graph.
        for node in graph:

            # Periksa setiap tetangga dari simpul saat ini beserta bobot edge-nya.
            for neighbor, weight in graph[node].items():

                # Relaksasi: jika jalur melewati simpul saat ini menghasilkan
                # jarak lebih kecil ke tetangga, perbarui jarak tetangga tersebut.
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Kembalikan dictionary berisi jarak terpendek ke seluruh simpul.
    return distances