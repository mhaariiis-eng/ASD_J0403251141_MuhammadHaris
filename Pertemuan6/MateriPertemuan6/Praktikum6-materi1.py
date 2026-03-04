#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# insertion sort : ascending
#======================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #Simpan data ke i sebagai key
        j = i - 1 #Inisialisasi j sebagai index sebelum i
        
        #geser
        while j>=0 and data[j] > key: #Loop selama j >= 0 dan data[j] lebih besar dari key
            data[j + 1] = data[j] #Geser data[j] ke kanan
            j -= 1
            #sisipkan key ke posisi yang benar
        data[j + 1] = key #Sisipkan
    return data
angka = [7,8,5,2,4,6]
print("Hasil Sorting:", insertion_sort(angka))