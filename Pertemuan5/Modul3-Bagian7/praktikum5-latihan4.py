#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#
#Latihan 4: Kombinasi Huruf 
#Program ini menghasilkan semua kombinasi huruf 'A' dan 'B' dengan panjang n menggunakan pendekatan rekursif
#=====================================================#

def kombinasi(n, hasil=""):
    """
    Fungsi rekursif untuk menghasilkan semua kemungkinan
    kombinasi huruf A dan B sepanjang n karakter.
    n     : jumlah karakter yang diinginkan
    hasil : string sementara yang sedang dibentuk (default kosong)
    """

    # BASE CASE → jika panjang string sudah mencapai n
    # Maka kombinasi dianggap selesai dan langsung ditampilkan
    if len(hasil) == n:
        print(hasil)
        return

    # RECURSIVE CASE → setiap langkah bercabang menjadi dua kemungkinan
    # Tambahkan "A" lalu lanjut rekursi
    kombinasi(n, hasil + "A")

    # Tambahkan "B" lalu lanjut rekursi
    kombinasi(n, hasil + "B")


kombinasi(4)  # Contoh: menghasilkan semua kombinasi 4 karakter (AAAA, AAAB, AABA, ..., BBBB)