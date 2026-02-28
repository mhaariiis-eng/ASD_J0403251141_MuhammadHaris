#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#Latihan 3: Mencari Nilai Maksimum Secara Rekursif
#program ini mencari nilai maksimum dari sebuah list menggunakan pendekatan rekursif
#=====================================================#


def cari_maks(data, index=0):
    """
    Fungsi untuk menentukan nilai terbesar dalam sebuah list
    dengan pendekatan rekursif.
    data  : list berisi angka
    index : posisi elemen yang sedang diproses (default mulai dari 0)
    """

    # BASE CASE → saat index sudah berada di elemen terakhir
    # Artinya tidak ada lagi elemen yang perlu dibandingkan
    if index == len(data) - 1:
        return data[index]

    # RECURSIVE CALL → mencari nilai maksimum dari sisa elemen
    # (posisi berikutnya sampai akhir list)
    maksimum_sisa = cari_maks(data, index + 1)

    # Membandingkan elemen sekarang dengan hasil maksimum dari sisa
    if data[index] > maksimum_sisa:
        return data[index]
    else:
        return maksimum_sisa


angka = [8, 4, 11, 6, 3]
print("Nilai terbesar dalam list adalah:", cari_maks(angka))