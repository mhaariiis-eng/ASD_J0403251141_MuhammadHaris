#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 3 - Membuat Traversal Preorder
#======================================================
#======================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#fungsi untuk melakukan traversal preorder
def preorder_traversal(node):
    if node is not None:
        print(node.data)  # Kunjungi root
        preorder_traversal(node.left)  # Kunjungi subtree kiri
        preorder_traversal(node.right)  # Kunjungi subtree kanan

#membuat tree
root = Node("A")

#membuat child level 1
root.left = Node("B")  # node anak kiri root
root.right = Node("C")  # node anak kanan root

#membuat child level 2
root.left.left = Node("D")  # node anak kiri dari B
root.left.right = Node("E")  # node anak kanan dari B

#menampilkan hasil traversal preorder
print("Hasil Traversal Preorder:")
preorder_traversal(root)

#Pembahasan :
#1. Traversal preorder adalah metode penelusuran tree di mana kita mengunjungi root terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan.
#2. Dalam contoh di atas, kita membuat sebuah tree dengan root "A" dan dua child "B" dan "C". Kemudian, kita menambahkan child untuk "B" yaitu "D" dan "E". Hasil traversal preorder akan mencetak urutan node sesuai dengan aturan preorder.
#3. Traversal preorder sering digunakan untuk membuat salinan dari sebuah tree atau untuk mendapatkan representasi prefix dari ekspresi dalam sebuah binary expression tree.