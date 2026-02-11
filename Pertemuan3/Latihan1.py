



class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan nilai/data dari node
        self.next = None    # Pointer ke node berikutnya (awalnya None)


class LinkedList:
    def __init__(self):
        self.head = None    # Head adalah node pertama (awal list), awalnya kosong

    def insert_at_end(self, data):
        new_node = Node(data)   # Membuat node baru dengan data yang diberikan

         # Jika linked list masih kosong
        if not self.head:
            self.head = new_node    # Node baru langsung jadi head
            return
        
        # Jika tidak kosong, cari node terakhir
        temp = self.head
        while temp.next:    # Selama masih ada node berikutnya
            temp = temp.next    # Pindah ke node berikutnya

        temp.next = new_node    # Node terakhir menunjuk ke node baru

    def delete_node(self, key):
        temp = self.head    # Mulai dari head

        # Jika node yang ingin dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next   # Head pindah ke node berikutnya
            temp = None     # Hapus referensi node lama

            print(f"Elemen {key} telah dihapus. ")
            return
    
        prev = None

        # Cari node yang memiliki data == key
        while temp and temp.data != key:
            prev = temp          # Simpan node sebelumnya
            temp = temp.next     # Pindah ke node berikutnya


          # Jika data tidak ditemukan
        if temp is None:
            print(f"Elemen {key} tidak ditemukan dalam linked list. ")
            return
        
        # Lewati node yang ingin dihapus
        prev.next = temp.next   # Node sebelumnya menunjuk ke node setelah yang dihapus
        temp = None             # Hapus referensi node
        print(f"Elemen {key} telah dihapus. ")

    def display(self):
        temp = self.head        # Mulai dari head
        while temp:         # Selama node masih ada
            print(temp.data, end= "--" )    # Cetak data
            temp = temp.next        # Pindah ke node berikutnya     
        print("Null")       # Penanda akhir linked list

#Program utama
if __name__ == "__main__":
    ll = LinkedList()   # Membuat objek LinkedList

    elements = input("Masukkan elemen untuk ke LinkedList: ")

        # Pisahkan input berdasarkan koma lalu masukkan satu per satu
    for elem in elements.split(","):
        
        ll.insert_at_end(int(elem.strip()))     # strip() untuk hapus spasi

    print("nIsi Linked List sebelum penghapusan: ")
    ll.display()

    key = int(input("Masukkan elemen yang ingin dihapus"))
    ll.delete_node(key)

    print("\nIsi Linked List setelah penghapusan: ")
    ll.display()