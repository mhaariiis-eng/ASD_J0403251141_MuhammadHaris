#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#Metri Rekursif : Call Stack
# Tracing Bilangan
#input 3
#Masuk 1 - 2 - 3
#Keluar
# 3-2-1 | 1-2-3
#
#=====================================================#

def hitung(n):

    #base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk", n)
    hitung(n-1)#recursive case
    print("Keluar", n)

print("Program Traving")
hitung(3)