#=================================================================#
# Tugas Hands-On Modul 1                                         
# Studi Kasus : Sistem Stok Barang Kantin (Berbasis File .txt)
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : Teknologi Rekayasa Perangkat Lunak B2
#=================================================================#

#Fungsi membaca data dari file Stok_Barang.txt

NAMA_file = "Stok_Barang.txt"

def baca_stok(Stok_Barang):

    stok_dict = {}

    try:
        with open(Stok_Barang, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                data = baris.split(",")

                if len(data) != 3:
                    continue

                kode, nama, stok_str = data

                try:
                    stok = int(stok_str)
                except ValueError:
                    continue

                stok_dict[kode] = {
                    "nama": nama, 
                    "stok": stok
                    }
    except FileNotFoundError:
        print(f"File {Stok_Barang} tidak ditemukan. Data dimulai dari kosong.")

    return stok_dict
    
#Fungsi Menyimpan data ke file Stok_Barang.txt

def simpan_stok(Stok_Barang, stok_dict):
    with open (Stok_Barang, "w", encoding="utf-8") as file:
        for kode in stok_dict:
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

#Fungsi Menampilkan Semua Data
def tampilkan_semua(stok_dict):
    if not stok_dict:
        print("Stok Barang Kosong.")
        return
    
    print("\nKode | Nama Barang | Stok")
    print("-" * 30)

    for kode in stok_dict:
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode: <10} | {nama: <20} | {stok: <5}")


#Fungsi Mencari Barang Berdasarkan Kode

def cari_barang(stok_dict):
    kode = input("Masukkab kode barang: ").strip()

    if kode in stok_dict:
        barang = stok_dict[kode]
        print("Barang ditemukan:")
        print("Nama :", barang["nama"])
        print("Stok :", barang["stok"])
    else:
        print("Barang tidak ditemukan.")

#Fungsi Menambahkan Barang Baru

def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka.")
        return
    
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

print("Barang berhasil ditambahkan.")


#Fungsi Mengupdate Stok Barang

def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkab Pilihan 1 atau 2: ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka. ")
        return
    
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak cukup untuk dikurangi. ")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid. ")

#Program Utama

def main():
    stok_barang = baca_stok(NAMA_file)
    
    while True:
        print("\n=== Menu Stok Kantin ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan dan keluar")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_file, stok_barang)
            print("Data berhasil disimpan. ")

        elif pilihan == "0":
            print("Terimakasih telah menggunakan program.")
            break

#Menjalankan program utama
if __name__ == "__main__":
    main() 