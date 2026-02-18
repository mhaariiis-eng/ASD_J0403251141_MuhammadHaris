#====================================================#
#
#           Nama : Muhammad Haris                    #
#                                                    #
#           NIM : J0403251141                         #
#
#    Prodi : Teknologi Rekayasa Perangkat Lunak
#
#    Implementasi dasar : Queue berbasis LinkedList
#
#=====================================================#

class Node:
    def __init__(self, data ):     #konstruktor    
        self.data = data    #Menyimpan nilai / data
        self.next = None    #pointer ke node berikutnya

#Queue dengan 2 pointer : head and tail
class QueueLL:
    def __init__(self):
        self.head = None    #Node paling depan
        self.tail = None    #Node paling belakang

    def is_empty(self):
        #queue kosong jika head = None
        return self.head is None

    def enqueue(self, data):
        #menambah data di belakang (tail)
        nodeBaru = Node(data)

        #Jika queue kosong, head dan tail menunjuk ke node yang sama
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #tail lama menunjuk ke node baru
        self.tail.next = nodeBaru
        #tail pindah ke node baru
        self.tail = nodeBaru

    def dequeue(self):
        #menghapus data dari depan
        data_terhapus = self.head.data #peek  stack
        #menggeser head ke node berikutnya
        self.head = self.head.next

        # Jika setelah geser head menjadi none, maka queue kosong
        #tail juga harus jadi none
        if self.head is None:
            self_tail = None

        return data_terhapus

    def tampilkan(self):
            #menampilkan isi queue dari head ke tail
        current = self.head
        print("Head ", end="-> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Tail")

#Instantiasi
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()