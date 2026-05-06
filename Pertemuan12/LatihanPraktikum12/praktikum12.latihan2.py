#==============================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq  # Modul bawaan Python untuk operasi min-heap (priority queue)

# Weighted graph yang direpresentasikan sebagai dictionary bersarang.
# Setiap key adalah nama simpul, dan value-nya adalah dictionary
# yang memetakan tetangga ke bobot edge masing-masing.
# Simpul 'D' tidak memiliki edge keluar (tidak ada tetangga).
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari simpul awal (start) ke semua simpul lain
    dalam graph menggunakan algoritma Dijkstra.
    """
    # Inisialisasi semua jarak dengan tak hingga (belum diketahui).
    # Artinya, awalnya semua simpul dianggap tidak dapat dijangkau.
    distances = {node: float('inf') for node in graph}

    # Jarak dari simpul awal ke dirinya sendiri selalu 0.
    distances[start] = 0

    # Priority queue diinisialisasi dengan simpul awal dan jarak 0.
    # Setiap elemen berupa tuple (jarak, nama_simpul) agar heapq
    # bisa mengurutkan berdasarkan jarak terkecil secara otomatis.
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil simpul dengan jarak terakumulasi terkecil dari antrian.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati pemrosesan jika jarak yang tersimpan di antrian
        # sudah lebih besar dari jarak terbaik yang tercatat.
        # Ini terjadi ketika ada duplikat entry lama di priority queue.
        if current_distance > distances[current_node]:
            continue

        # Telusuri semua tetangga dari simpul yang sedang diproses.
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak total jika melewati simpul saat ini menuju tetangga.
            distance = current_distance + weight

            # Jika jalur baru ini lebih pendek dari yang sudah tercatat,
            # perbarui jarak terpendek dan masukkan ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Kembalikan dictionary berisi jarak terpendek ke seluruh simpul.
    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ============================================================
# Jawaban Analisis
# ============================================================

# 1. Berapa jarak terpendek dari A ke B?
#    Jaraknya adalah 4.
#    Hanya ada satu jalur yang bisa dilalui, yaitu langsung A → B
#    dengan bobot edge sebesar 4.

# 2. Berapa jarak terpendek dari A ke C?
#    Jaraknya adalah 2.
#    Sama seperti sebelumnya, hanya ada satu jalur langsung A → C
#    dengan bobot edge sebesar 2.

# 3. Berapa jarak terpendek dari A ke D?
#    Jaraknya adalah 3.
#    Didapat dari jalur A → C → D: bobot A→C (2) ditambah bobot C→D (1)
#    menghasilkan total 3.

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jalur A → B → D memiliki total bobot 4 + 5 = 9.
#    Jalur A → C → D memiliki total bobot 2 + 1 = 3.
#    Meski keduanya melewati jumlah edge yang sama (2 edge), bobot
#    masing-masing edge di jalur via C jauh lebih kecil.
#    Dijkstra mengambil keputusan berdasarkan akumulasi bobot terkecil,
#    bukan sekadar jumlah langkah yang ditempuh.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Priority queue (min-heap) memastikan simpul dengan jarak terakumulasi
#    terkecil selalu diproses lebih dahulu. Setiap entry disimpan sebagai
#    pasangan (jarak, simpul), dan heapq.heappop() secara otomatis mengambil
#    entry dengan jarak terkecil. Mekanisme ini menjamin bahwa ketika suatu
#    simpul selesai diproses, jarak yang tercatat sudah merupakan yang paling
#    optimal — tanpa perlu mengevaluasi ulang semua kemungkinan jalur.
#    Tanpa struktur ini, algoritma terpaksa melakukan pencarian linear yang
#    jauh lebih lambat: kompleksitas O(V²) dibanding O((V + E) log V)
#    dengan priority queue.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Dijkstra dibangun di atas asumsi bahwa begitu sebuah simpul diambil
#    dari priority queue, jaraknya sudah final dan tidak akan berkurang lagi.
#    Asumsi ini hanya berlaku selama semua bobot edge bernilai positif,
#    karena menambahkan nilai positif tidak mungkin memperkecil jarak
#    yang sudah ditemukan sebelumnya.
#    Jika terdapat edge berbobot negatif, jalur yang tampak lebih panjang
#    di awal bisa saja berubah menjadi lebih pendek setelah melewati edge
#    negatif tersebut. Akibatnya, simpul yang sudah "selesai" bisa memiliki
#    jarak optimal yang lebih kecil melalui jalur lain, dan Dijkstra akan
#    memberikan hasil yang keliru.
#    Untuk kasus seperti ini, algoritma Bellman-Ford lebih sesuai karena
#    ia mengevaluasi seluruh edge secara berulang sebanyak (V-1) kali
#    sehingga dapat menangani bobot negatif dengan benar.