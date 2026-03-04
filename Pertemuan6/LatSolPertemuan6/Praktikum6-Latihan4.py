#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# Latihan 4 . Memahami Kode Program (Merge Sort)

#======================================================

from heapq import merge

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return list(merge(left_sorted, right_sorted))


#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?

#Jawaban:
#1. Base case adalah kondisi penghentian dalam fungsi rekursif. Pada merge sort, kondisi ini terjadi ketika jumlah elemen dalam data kurang dari atau sama dengan satu. Pada tahap ini, data dianggap sudah terurut sehingga tidak perlu dibagi atau diproses lagi.
#2. Fungsi memanggil dirinya sendiri karena merge sort menggunakan pendekatan rekursif untuk memecah data menjadi bagian-bagian yang lebih kecil. Setiap bagian dipecah terus hingga mencapai base case, kemudian hasilnya digabung kembali secara bertahap hingga membentuk data yang sudah terurut secara keseluruhan.
#3. Fungsi merge() bertujuan untuk menggabungkan dua bagian data yang sudah terurut menjadi satu urutan yang tetap teratur. Proses ini dilakukan dengan membandingkan elemen dari kedua bagian dan menyusunnya kembali dalam urutan yang sesuai.