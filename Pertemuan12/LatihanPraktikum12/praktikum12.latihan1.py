#==============================================
#Nama  : Muhammad Haris
#NIM   : J0403251141
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================


# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
 
# Mendefinisikan weighted graph menggunakan dictionary bersarang.
# Setiap key luar adalah nama simpul (node), dan value-nya adalah
# dictionary yang berisi tetangga beserta bobot (cost) masing-masing edge.
# Contoh: 'A' terhubung ke 'B' dengan bobot 4, dan ke 'C' dengan bobot 2.
# Simpul 'D' tidak memiliki tetangga (tidak ada edge keluar).
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
 
# Menghitung total bobot untuk dua kemungkinan jalur dari A ke D.
# jalur_1 menelusuri rute A -> B -> D:
#   ambil bobot edge A ke B, lalu tambahkan bobot edge B ke D.
jalur_1 = graph['A']['B'] + graph['B']['D']   # 4 + 5 = 9
 
# jalur_2 menelusuri rute A -> C -> D:
#   ambil bobot edge A ke C, lalu tambahkan bobot edge C ke D.
jalur_2 = graph['A']['C'] + graph['C']['D']   # 2 + 1 = 3
 
# Menampilkan total bobot masing-masing jalur ke layar.
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
 
# Membandingkan kedua jalur untuk menentukan mana yang lebih pendek.
# Jika bobot jalur_1 lebih kecil, cetak bahwa rute A->B->D adalah terpendek.
# Sebaliknya (termasuk jika sama), cetak bahwa rute A->C->D adalah terpendek.
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
 
 
# ============================================================
# Jawaban Analisis
# ============================================================
 
# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobotnya adalah 9.
#    Rincian: edge A→B memiliki bobot 4, ditambah edge B→D berbobot 5,
#    sehingga jumlahnya menjadi 4 + 5 = 9.
 
# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobotnya adalah 3.
#    Rincian: edge A→C memiliki bobot 2, ditambah edge C→D berbobot 1,
#    sehingga jumlahnya menjadi 2 + 1 = 3.
 
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur terpendek adalah A -> C -> D dengan total bobot 3.
#    Karena nilai jalur_1 (9) tidak lebih kecil dari jalur_2 (3),
#    kondisi (jalur_1 < jalur_2) bernilai False, dan program masuk
#    ke blok else, sehingga mencetak "Jalur terpendek adalah A -> C -> D".
 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah
#    edge yang paling sedikit?
#
#    Dalam weighted graph, setiap edge memiliki bobot yang merepresentasikan
#    nilai tertentu — misalnya jarak, waktu tempuh, atau biaya perjalanan.
#    Menghitung jumlah edge hanya mencerminkan banyaknya langkah yang diambil,
#    bukan seberapa "mahal" atau "jauh" perjalanan tersebut secara keseluruhan.
#
#    Pada contoh ini, kedua jalur sama-sama melewati 2 edge, tetapi total
#    bobotnya sangat berbeda: A→B→D bernilai 9, sedangkan A→C→D hanya 3.
#    Artinya, dua jalur dengan jumlah langkah yang identik bisa memiliki biaya
#    yang jauh berbeda tergantung bobot tiap edge-nya.
#
#    Dalam skenario nyata seperti sistem navigasi atau jaringan komputer,
#    mengabaikan bobot dan hanya mengandalkan jumlah langkah dapat menghasilkan
#    rute yang secara teknis singkat namun justru lebih lambat atau lebih mahal.
#    Itulah mengapa algoritma seperti Dijkstra dirancang untuk meminimalkan
#    total bobot, bukan sekadar jumlah edge yang dilalui.