#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#Materi Rekursif : Faktorial
#Recursive case => 3! = 3 x 2 x 1
#Base case => 0 berhenti
#
#=====================================================#

def faktorial(n):
    if n == 0:
        return 1
    
    #recursive case
    return n*faktorial(n-1)    #n-1*n-2*n-3........n-?

print("Program Faktorial")
print("Hasil Faktorial : ", faktorial(3))
