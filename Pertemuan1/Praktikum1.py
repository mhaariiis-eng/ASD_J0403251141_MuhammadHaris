#============================================#
# Praktikum 1 : Konsep ADT dan File Handling #
# Latihan Dasar 1 : Membaca seluruh isi file #
#============================================#

# Membuka file 'Data_Mahasiswa.txt' dalam mode read ('r' = read/baca)
# encoding='utf-8' untuk mendukung karakter khusus
# 'as file' menyimpan objek file dalam variabel 'file'
with open('Data_Mahasiswa.txt', 'r', encoding='utf-8') as file:
    # Membaca SELURUH isi file menjadi string tunggal
    isi_file = file.read()
    # Catatan: file.read() menyimpan semua konten termasuk karakter newline (\n)
    
    # Menampilkan isi file yang sudah dibaca ke layar (console/terminal)
    print(isi_file)

# Menampilkan header untuk hasil analisis
print("=====Hasil Read=====")
# Menampilkan tipe data dari isi_file (akan menampilkan <class 'str'> karena read() mengembalikan string)
print("Tipe data isi_file :", type(isi_file))
# Menampilkan jumlah karakter dalam isi_file (termasuk spasi, tab, newline, dll)
print("Jumlah kata :", len(isi_file))
# Menampilkan jumlah baris: count('\n') menghitung jumlah newline + 1 untuk baris terakhir
print("Jumlah Baris :", isi_file.count('\n') + 1)

# Membaca file perbaris (line by line)
print("=====Membaca File Perbaris=====")
# Inisialisasi variabel counter untuk menghitung jumlah baris
jumlah_baris = 0
# Membuka file dalam mode read
with open('Data_Mahasiswa.txt', 'r', encoding='utf-8') as file:
    # Loop untuk membaca setiap baris dalam file secara otomatis
    for baris in file:
        # Increment counter setiap kali membaca satu baris
        jumlah_baris += 1
        # Menghapus karakter newline (\n) dari akhir baris
        baris = baris.replace('\n', '')
        # Menampilkan baris dengan nomor baris dan menghapus whitespace di awal/akhir (.strip())
        print(f"Baris {jumlah_baris}: {baris.strip()}")

#=============================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data (memisah data dengan koma)
#=============================================

# Membuka file dalam mode read
with open('Data_Mahasiswa.txt', 'r', encoding='utf-8') as file:
    # Loop untuk membaca setiap baris dalam file
    for baris in file:
        # Memisahkan (split) data berdasarkan delimiter koma (',') menjadi list
        # Contoh: "12345,Budi,85" menjadi ['12345', 'Budi', '85']
        baris = baris.split(',')
        # Unpack (destructuring) list ke tiga variabel terpisah
        NIM, Nama, Nilai = baris
        # Menampilkan data yang sudah dipisah dalam format yang rapi
        print("NIM :", NIM, "| Nama :", Nama , "| Nilai :", Nilai)


#================================================================#
# Praktikum 1 : Konsep ADT dan File Handling                     #
# Latihan Dasar 3 : Membaca File dan Menyimpan data ke dalam List#
#================================================================#

# Inisialisasi list kosong untuk menyimpan semua data mahasiswa
data_list = []

# Membuka file dalam mode read
with open('Data_Mahasiswa.txt', 'r', encoding='utf-8') as file:
    # Loop untuk membaca setiap baris dalam file
    for baris in file:
        # Memisahkan data berdasarkan delimiter koma (',')
        baris = baris.split(',')
        # Unpack data ke tiga variabel
        NIM,Nama,Nilai = baris
        # Menambahkan data dalam bentuk list ke dalam data_list
        # int(Nilai) mengkonversi Nilai dari string menjadi integer (angka)
        data_list.append([NIM,Nama,int(Nilai)])

# Menampilkan header
print("=====Data Mahassiswa dalam List :=====")
# Menampilkan seluruh list yang berisi data mahasiswa
print(data_list)

# Menampilkan header untuk informasi jumlah record
print("=====Jumlah Record dalam List :=====")
# Menampilkan jumlah elemen (record) dalam list menggunakan len()
print("Jumlah Record :", len(data_list))

# Menampilkan header untuk contoh akses data
print("=====Menampilkan Data Record Tertentu dari List :=====")
# Menampilkan record pada index ke-1 (elemen ke-2, karena indexing dimulai dari 0)
print("Contoh Record :", data_list[1])

#======================================================================#
# Praktikum 1 : Konsep ADT dan File Handling                           #
# Latihan Dasar 4 : Membaca File dan Menyimpan data ke dalam Dictionary#
#======================================================================#

# Inisialisasi dictionary kosong untuk menyimpan data dengan key-value pairs
data_dict = {}
# Membuka file dalam mode read
with open('Data_Mahasiswa.txt', 'r', encoding='utf-8') as file:
    # Loop untuk membaca setiap baris dalam file
    for baris in file:
        # Menghapus karakter koma dari akhir baris (jika ada) menggunakan strip()
        baris = baris.strip(',')
        # Memisahkan data berdasarkan delimiter koma (',')
        NIM,Nama,Nilai = baris.split(",")
        # Menambahkan data ke dictionary dengan:
        # - Key: NIM (nomor induk mahasiswa)
        # - Value: dictionary dengan key 'Nama' dan 'Nilai'
        # - int(Nilai) mengkonversi string nilai menjadi integer
        data_dict[NIM] = {'Nama': Nama, 'Nilai': int(Nilai)}

# Menampilkan seluruh dictionary yang berisi data mahasiswa
print("Data Mahasiswa dalam Dictionary :")
# Menampilkan isi dictionary ke layar
print(data_dict)