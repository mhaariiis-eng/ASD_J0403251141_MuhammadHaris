#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 4 - Membuat Traversal inorder
#======================================================
#======================================================

#Class node adalah dasar dari tree


class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#membuat fungsi innorder traversal : left, root, right
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)  # Kunjungi subtree kiri
        print(node.data, end=" ")  # Kunjungi root
        inorder_traversal(node.right)  # Kunjungi subtree kanan 

#Membuat tree
#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")  # node anak kiri root
root.right = Node("C")  # node anak kanan root

#membuat child level 2
root.left.left = Node("D")  # node anak kiri dari B
root.left.right = Node("E")  # node anak kanan dari B

print("Hasil Traversal Inorder:")
inorder_traversal(root)

#Pembahasan :
#1. Traversal inorder adalah metode penelusuran tree di mana kita mengunjungi subtree kiri terlebih dahulu, kemudian root, dan terakhir subtree kanan.
#2. Dalam contoh di atas, kita membuat sebuah tree dengan root "A" dan dua child "B" dan "C". Kemudian, kita menambahkan child untuk "B" yaitu "D" dan "E". Hasil traversal inorder akan mencetak urutan node sesuai dengan aturan inorder.
#3. Traversal inorder sering digunakan untuk mendapatkan urutan data yang terurut dalam sebuah binary search tree (BST), karena dalam BST, nilai pada subtree kiri selalu lebih kecil dari root, dan nilai pada subtree kanan selalu lebih besar dari root.