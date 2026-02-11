class NodeDLL:
    def __init__(self, data):
        self.data = data    # Menyimpan nilai/data node
        self.next = None    # Pointer ke node berikutnya
        self.prev = None    # Pointer ke node sebelumnya

class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Node pertama
        self.tail = None    # Node terakhir (biar insert lebih cepat O(1))
    
    def insert_at_end(self, data):
        new_node = NodeDLL(data)    # Membuat node baru

        # Jika list masih kosong
        if not self.head:
            self.head = self.tail = new_node    # Head dan tail menunjuk ke node pertama
            return
        
        # Hubungkan tail lama ke node baru
        self.tail.next = new_node   # Tail lama menunjuk ke node baru
        new_node.prev = self.tail = self.tail   # Node baru menunjuk balik ke tail lama
        self.tail = new_node       # Update tail ke node baru

    def search(self, key):
        temp = self.head     # Mulai dari head

         # Traversal maju
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam linked list.")
                return      # Berhenti kalau ketemu
            temp = temp.next

        # Jika sudah sampai akhir dan tidak ketemu
        print(f"Elemen {key} tidak ditemukan dalam linked list. ")

    def display(self):
        temp = self.head        # Mulai dari head
        while temp:
            print(temp.data, end=" ->- ")    # Cetak data

            temp = temp.next        # Pindah ke node berikutnya

        print("Null")       # Penanda akhir list

#Program utama

dll = DoublyLinkedList()

# Input elemen
input_data = input("Masukkan elemen ke dalam double linked list: ")
data_list = input_data.split(",")
for item in data_list:
    dll.insert_at_end(int(item.strip()))    # strip() untuk hilangkan spasi

    print("\nIsi Doubly Linked List:")
    dll.display()

#input pencarian
cari = int(input("Masukkan elemen yang ingin dicaari: "))
dll.search(cari)