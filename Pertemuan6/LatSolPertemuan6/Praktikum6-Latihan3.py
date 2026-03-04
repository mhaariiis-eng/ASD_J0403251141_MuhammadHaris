#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# Latihan 3 . Tracing Insertion Sort
#======================================================

def insertion_sort(data):
    #melihat data awal
    print("Data Awal:", data)
    print("="*50)

    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #Simpan data ke i sebagai key
        j = i - 1 #Inisialisasi j sebagai index sebelum i

        print("Iterasi ke-", i)
        print("NilaiKey:", key)
        print("Bagian kiri data yang sudah terurut:", data[:i])
        print("Bagian kanan data yang belum terurut:", data[i:])
        
        #geser
        while j>=0 and data[j] > key: #Loop selama j >= 0 dan data[j] lebih besar dari key
            data[j + 1] = data[j] #Geser data[j] ke kanan
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j + 1] = key 

        print("Setelah disisipkan:", data)
        print("="*50)

    return data

print("Hasil Sorting:", insertion_sort([5, 2, 4, 6, 1, 3,]))


#Buat program dengan menggunakan algoritma insertion sort
#Tracing dengan data = [5, 2, 4, 6, 1, 3]

#Soal:
#1. Tuliskan isi list setelah iterasi i = 1.
#2. Tuliskan isi list setelah iterasi i = 3.
#3. Berapa kali pergeseran terjadi pada iterasi i = 4?

#Jawaban:
#1. Setelah iterasi i = 1, isi list menjadi [2, 5, 4, 6, 1, 3]. Pada tahap ini, elemen 2 dibandingkan dengan 5 dan dipindahkan ke posisi yang benar di depan 5 sehingga dua elemen pertama menjadi terurut.
#2. Setelah iterasi i = 3, isi list adalah [2, 4, 5, 6, 1, 3]. Pada iterasi ini, nilai 6 tidak mengalami pergeseran karena sudah lebih besar dari elemen-elemen sebelumnya, sehingga posisinya sudah benar dan tidak terjadi perubahan susunan.
#3. Pada iterasi i = 4 terjadi 4 kali pergeseran. Elemen 6, 5, 4, dan 2 masing-masing digeser satu posisi ke kanan untuk memberi ruang bagi nilai 1 yang akan ditempatkan di awal list.