#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#Studi Kasus : Sistem Antrian Layanan Akademik
#Implementasi : Queue
#Enqueue : memindahkan pointer rear (nambah data dari belakang)
#Dequeue : memindahkan pointer front (menghapus data dari depan)
#Head -> Tail
#
#=====================================================#


#1. Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__ (self, nim, nama):
        self.nim = nim   #Menyimpan NIM Mahasiswa
        self.nama = nama  #Menyimpan Nama Mahasiswa
        self.next = None  #pointer ke node berikutnya

#2. Mendefinisikan queue, terdiri dari head dan tail
class queueAkademik:
    def __init__ (self):
        self.head = None
        self.tail = None

    def is_empty(self):
        #Ketika queue kosong maka head = tail = none
        return self.head is None
    
    #Menambahkan data baru ke bagian belakang (tail)
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        #Jika data baru masuk data queue yang kosong maka data baru = head tail
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakkan setelah tail kemudian dijadikan sebagai tail
        
        self.tail.next = nodeBaru
        self.tail = nodeBaru


#Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang dilayani")
            return None
            
        #Lihat data bagian head, simpan di variabel data yang akan dihapus(dilayani)
        node_dilayani = self.head

        #geser pointer head ke next head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return node_dilayani

    def tampilkan(self):
        print("Daftar Antrian Mahasiswa ( Head -> Tail) : ")
        current = self.head
        no = 1
        while current is not None:
            print(f"{no}. NIM{current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1

def main():
    q = queueAkademik()

    while True:
        print("Sistem Antrian Akademik")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("masukkan Nim :").strip()
            nama = input("masukkan Nama :").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani dengan NIM {dilayani.nim} dan nama {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Terimakasih telah menggunakan program")
            break
        else:
            print("Pilihan tidak valid. Coba lagi 1-4 ")

if __name__ == "__main__":
    main()