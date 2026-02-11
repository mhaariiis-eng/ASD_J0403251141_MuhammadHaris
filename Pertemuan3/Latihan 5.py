class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan nilai node
        self.next = None    # Pointer ke node berikutnya


class LinkedListReverse:
    def __init__(self):
        self.head = None    # Node pertama (awal linked list)

    def insert_at_end(self, data):
        new_node = Node(data)    # Membuat node baru
        
        # Jika list kosong
        if not self.head:
            self.head = new_node
            return
        
        # Jika tidak kosong, cari node terakhir
        temp = self.head
        while temp.next:    # Selama masih ada node berikutnya
            temp = temp.next
        temp.next = new_node    # Node terakhir menunjuk ke node baru

    def reverse(self):
        prev = None             # Node sebelumnya (awal = None)
        current = self.head # Mulai dari head

        # Loop sampai current habis (None)
        while current:
            next_node = current.next    # Simpan node berikutnya dulu
            current.next = prev     # Balik arah pointer
             # Sekarang node menunjuk ke belakang

            prev = current      # Geser prev ke current
            current = next_node     # Geser current ke node berikutnya

        # Setelah loop selesai,
        # prev akan berada di node terakhir (yang jadi head baru)
        self.head = prev

        # Intinya:
        # Kita membalik arah pointer satu per satu.
        # Bukan memindahkan data, tapi membalik link antar node.

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -- ")
            temp = temp.next
        print("Null")

# Program utama
if __name__ == "__main__":
    elements = input("Masukkan elemen untuk Linked List: ")
    llr = LinkedListReverse()
    # Masukkan elemen ke linked list
    for elem in elements.split(","):
        llr.insert_at_end(int(elem.strip()))    # strip() biar aman kalau ada spasi

    print("\nLinked List sebelum dibalik:", end=" ")
    llr.display()

    llr.reverse()    # Proses pembalikan
    
    print("Linked list setelah dibalik:", end=" ")
    llr.display()
