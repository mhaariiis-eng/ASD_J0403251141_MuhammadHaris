#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# Latihan 2 . Melengkapi Potongan Kode
#======================================================


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    return data



#Soal:
#  1. Lengkapi kondisi agar menjadi sorting ascending.
#  2. Ubah agar menjadi descending.

#Jawaban:
# 1. Untuk menghasilkan sorting ascending, kondisi pada while harus data[j] > key. Kondisi ini memastikan bahwa setiap elemen di sebelah kiri yang lebih besar dari key akan digeser satu posisi ke kanan. Setelah proses pergeseran selesai, baris data[j + 1] = key berfungsi untuk menempatkan kembali nilai key ke posisi yang sudah tepat dalam urutan yang semakin terurut dari kecil ke besar.
# 2. Untuk mengubah menjadi sorting descending, kondisi pada while diubah menjadi data[j] < key. Dengan kondisi ini, elemen yang lebih kecil dari key akan digeser ke kanan karena dalam urutan menurun elemen yang lebih besar harus berada di kiri. Setelah semua elemen yang tidak sesuai posisi digeser, baris data[j + 1] = key tetap digunakan untuk menyisipkan key ke lokasi yang benar dalam urutan besar ke kecil.