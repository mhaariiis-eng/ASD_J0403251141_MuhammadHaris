#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# Latihan 5 . Melengkapi Fungsi Merge
#======================================================


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


#Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#2. Jelaskan fungsi result.extend().

#Jawaban:
#1. Untuk menghasilkan urutan ascending, kondisi pada if harus membandingkan apakah elemen pada list kiri lebih kecil daripada elemen pada list kanan, yaitu left[i] < right[j]. Jika kondisi ini terpenuhi, maka elemen dari left dimasukkan terlebih dahulu ke dalam result karena dalam urutan naik, nilai yang lebih kecil harus berada di depan. Jika tidak, maka elemen dari right yang dimasukkan. Perbandingan ini menjaga agar hasil penggabungan tetap terurut dari kecil ke besar.
#2. Fungsi result.extend() digunakan untuk menambahkan seluruh sisa elemen dari salah satu list ke dalam result. Ketika perulangan berhenti, pasti salah satu list sudah habis lebih dulu, sementara list lainnya masih memiliki elemen yang belum diproses. Karena bagian tersebut sudah dalam keadaan terurut, semua elemennya bisa langsung ditambahkan tanpa perlu dibandingkan lagi. Dengan demikian, seluruh elemen dari kedua list tetap masuk ke dalam hasil akhir tanpa ada yang terlewat.
