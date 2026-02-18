#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak
#
#
#Implementasi Dasar : Node pada Linked List
#
#=====================================================#


class Node:
    def __init__(self, data ):     #konstruktor    
        self.data = data    #Menyimpan nilai / data
        self.next = None    #pointer ke node berikutnya

#1. Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2. Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3. Menentukan Head Node
head = nodeA

#4. Traversal : menelusuri dari head sampai None
current = head
while current is not None:
    print(current.data)        #Menampilkan Data pada Node saat ini
    current = current.next     #Pindah ke node berikutnya

#Implementasi Dasar: LinkedList = Insert Awal 

class LinkedList:   #Class implementasi Stack
    def __init__(self):
        self.head = None #awalnya kosong

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek  stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah : "), data_terhapus

    def insert_awal(self, data):    #push dalam stack
        #1) buat node baru
        nodeBaru = Node(data) #panggil class Node

        #2) node baru menunjukkan ke head lama
        nodeBaru.next = self.head

        #3)head pindah ke node baru
        self.head = nodeBaru

    def tampilkan(self):    #implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList() #instantiasi objek ke class LinkedList
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()