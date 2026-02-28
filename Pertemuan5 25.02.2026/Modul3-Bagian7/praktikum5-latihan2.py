#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
# Latihan 2: Tracing Rekursi 
# Program ini menunjukkan urutan eksekusi rekursi dengan print sebelum dan sesudah pemanggilan diri
#=====================================================#


def countdown(n):
 # BASE CASE: kondisi berhenti (n = 0)
 if n == 0:
    print("Selesai")  # Ketika n=0, program berhenti
    return
 
 # Eksekusi ini SEBELUM pemanggilan diri (print "Masuk" pertama)
 print("Masuk:", n)
 
 # RECURSIVE CALL: memanggil diri dengan n lebih kecil
 countdown(n - 1)
 
 # Eksekusi ini SETELAH pemanggilan diri selesai (print "Keluar" kemudian)
 print("Keluar:", n)

countdown(9)