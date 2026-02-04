#======================================================================#
# Praktikum 2 : Konsep ADT dan File Handling                           #
# Latihan Dasar 1 Membuat fungsi load data mahasiswa                   #
#======================================================================#


def baca_data_mahasiswa(nama_file):
    data_dict = {}

    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            parts = baris.split(',')

            if len(parts) != 3:
                continue

            nim, nama, nilai_str = parts

            try:
                nilai = int(nilai_str)
            except ValueError:
                nilai = nilai_str

            data_dict[nim] = {
                'Nama': nama,
                'Nilai': nilai
            }

    return data_dict

buka_data = baca_data_mahasiswa('data_mahasiswa.txt')
#print("Jumlah data mahasiswa:", len(buka_data))

#======================================================================#
# Praktikum 2 : Konsep ADT dan File Handling                           #
# Latihan Dasar 2 : Membaca File dan Menyimpan data ke dalam Dictionary#
#======================================================================#

def tampilkan_data_mahasiswa(data_dict):

    if len(data_dict) == 0:
        print("Tidak ada data mahasiswa untuk ditampilkan.")
        return
    
    #Mrmbuat header tabel
    print("\n======== Data Mahasiswa ========")
    print(f"{'NIM': <10} | {'Nama': <12} | {'Nilai': >5}")
    print("-" * 32) #membuat garis pemisah

    #untuk tampilan yang rapi, atur f-string formating
        #('NIM': <10)  : rata kiri dengan lebar 10 karakter
        #('Nama': <12) : rata kiri dengan lebar 12 karakter
        #('Nilai': >5) : rata kanan dengan lebar 5 karakter


    for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['Nama']
            nilai = data_dict[nim]['Nilai']
            print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

#tampilkan_data_mahasiswa(buka_data)

#======================================================================#
# Praktikum 2 : Konsep ADT dan File Handling                           #
# Latihan Dasar 3 : Membuat fungsi mencari data                        #
#======================================================================#

def cari_data_mahasiswa(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("\nMasukkan NIM yang dicari : ").strip()


    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['Nama']
        nilai = data_dict[nim_cari]['Nilai']

        print("\nData Mahasiswa Ditemukan :")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData Mahasiswa Tidak Ditemukan.")
    
#cari_data_mahasiswa(buka_data)

#======================================================================#
# Praktikum 2 : Konsep ADT dan File Handling                           #
# Latihan Dasar 4 : Membuat fungsi update nilai                        #
#======================================================================#

def update_nilai_mahasiswa(data_dict):
    #Cari data mahasiswa berdasarkan NIM yang akan di update nilainya
    nim_update = input("\nMasukkan NIM Mahasiswa yang akan diupdate nilainya : ").strip()

    if nim_update not in data_dict:
        print("\nData Mahasiswa Tidak Ditemukan.")
        return
    try:
        nilai_baru = int(input("Masukkan Nilai Baru (0-100) : ").strip())
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100. Update dibatalkan.")
        return

    nilai_lama = data_dict[nim_update]['Nilai']
    data_dict[nim_update]['Nilai'] = nilai_baru

    print(f"\nUpdate Berhasil!. Nilai {nim_update} diubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai_mahasiswa(buka_data)

#======================================================================#
# Praktikum 2 : Konsep ADT dan File Handling                           #
# Latihan Dasar 5 : Menyimpan data kembali ke file                     #
#======================================================================#

def simpan_data_mahasiswa(data_dict, nama_file):
    with open(nama_file, 'w') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['Nama']
            nilai = data_dict[nim]['Nilai']
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data_mahasiswa(buka_data, 'data_mahasiswa.txt')
print("\nData mahasiswa telah disimpan kembali ke file 'data_mahasiswa.txt'.")

def main():


    #menjalankan semua fungsi di atas secara berurutan
    buka_data = baca_data_mahasiswa('data_mahasiswa.txt')

while True:
    print('\n===Menu Data Mahasiswa===')
    print('1. Tampilkan Data Mahasiswa')
    print('2. Cari Data Mahasiswa')
    print('3. Update Nilai Mahasiswa')
    print('4. Simpan Data ke File')
    print('0. Keluar dari Program')

    pilihan = input("Pilih menu (1-5) : ").strip()

    if pilihan == '1':
        tampilkan_data_mahasiswa(buka_data)

    elif pilihan == '2':
        cari_data_mahasiswa(buka_data)

    elif pilihan == '3':
        update_nilai_mahasiswa(buka_data)

    elif pilihan == '4':
        simpan_data_mahasiswa(buka_data, 'data_mahasiswa.txt')
        
    elif pilihan == '0':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
    