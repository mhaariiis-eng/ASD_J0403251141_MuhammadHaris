#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#======================================================
# Latihan 1 . Memahami Kode Program (Insertion Sort)
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
#1. Mengapa perulangan dimulai dari indeks 1
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?

#Jawaban:
#1. Perulangan dimulai dari indeks 1 karena elemen pertama dianggap sebagai bagian yang sudah terurut. Insertion sort bekerja dengan menyisipkan elemen ke dalam bagian kiri yang sudah terurut, sehingga proses dimulai dari elemen kedua untuk dibandingkan dengan elemen sebelumnya.
#2. Variabel key berfungsi sebagai penyimpan sementara nilai yang sedang diproses. Nilai ini ditahan agar elemen-elemen yang lebih besar dapat digeser terlebih dahulu, lalu key ditempatkan pada posisi yang sesuai setelah pergeseran selesai.
#3. Perulangan while digunakan karena jumlah pergeseran tidak dapat ditentukan di awal. Proses pergeseran berlangsung selama kondisi tertentu masih terpenuhi, yaitu selama indeks masih valid dan elemen di kiri lebih besar dari key. While lebih fleksibel untuk kondisi yang bergantung pada keadaan dinamis seperti ini.
#4. Di dalam blok while terjadi proses pergeseran elemen ke kanan. Elemen yang lebih besar dari key dipindahkan satu posisi agar memberi ruang bagi key untuk ditempatkan di posisi yang benar.