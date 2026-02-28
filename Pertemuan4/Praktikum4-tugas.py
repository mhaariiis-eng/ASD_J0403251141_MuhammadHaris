#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#Studi Kasus : Sistem Antrian Bengkel
#Implementasi : Queue
#Enqueue : memindahkan pointer rear (nambah data dari belakang)
#Dequeue : memindahkan pointer front (menghapus data dari depan)
#Head -> Tail
#
#=====================================================#

# Class Node: merepresentasikan satu elemen dalam linked list
class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None  # pointer ke node berikutnya


# Class QueueBengkel: implementasi Queue menggunakan Linked List
# Menggunakan dua pointer: head (awal antrian) dan tail (akhir antrian)
class QueueBengkel:
    def __init__(self):
        self.head = None
        self.tail = None

    # Mengecek apakah queue kosong
    def is_empty(self):
        return self.head is None

    # Menambahkan pelanggan ke belakang antrian (enqueue)
    def enqueue(self, no, nama, servis):
        node_baru = Node(no, nama, servis)

        if self.is_empty():
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

        print(f"Pelanggan {nama} (No {no}) berhasil ditambahkan ke antrian.")

    # Melayani pelanggan paling depan (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan untuk dilayani.")
            return None

        pelanggan_keluar = self.head

        no_keluar = pelanggan_keluar.no
        nama_keluar = pelanggan_keluar.nama
        servis_keluar = pelanggan_keluar.servis

        # Geser head ke node berikutnya
        self.head = self.head.next

        # Jika setelah digeser menjadi kosong
        if self.head is None:
            self.tail = None

        print(f"Melayani pelanggan: No {no_keluar}, Nama {nama_keluar}, Servis {servis_keluar}")
        return pelanggan_keluar

    # Menampilkan seluruh isi antrian
    def tampilkan(self):
        if self.is_empty():
            print("Saat ini antrian masih kosong.")
            return

        print("\n===== DAFTAR ANTRIAN =====")
        current = self.head
        urut = 1

        while current is not None:
            print(f"{urut}. {current.nama} - {current.servis}")
            current = current.next
            urut += 1


# Program utama
def main():
    q = QueueBengkel()

    while True:
        print("\n=== MENU SISTEM ANTRIAN ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("Nomor antrian: ")
            nama = input("Nama pelanggan: ")
            servis = input("Jenis servis: ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")
            

if __name__ == "__main__":
    main()