#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 5 - Membuat Traversal postorder
#======================================================
#======================================================

#Class node adalah dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#membuat traversal postorder : left, right, root
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # Kunjungi subtree kiri
        postorder_traversal(node.right)  # Kunjungi subtree kanan
        print(node.data, end=" ")  # Kunjungi root

#membuat tree

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")  # node anak kiri root
root.right = Node("C")  # node anak kanan root

#membuat child level 2
root.left.left = Node("D")  # node anak kiri dari B
root.left.right = Node("E")  # node anak kanan dari B

#menampilkan hasil traversal postorder
print("Hasil Traversal Postorder:")
postorder_traversal(root)

#Pembahasan :
#1. Traversal postorder adalah metode penelusuran tree di mana kita mengunjungi subtree kiri terlebih dahulu, kemudian subtree kanan, dan terakhir root.
#2. Dalam contoh di atas, kita membuat sebuah tree dengan root "A" dan dua child "B" dan "C". Kemudian, kita menambahkan child untuk "B" yaitu "D" dan "E". Hasil traversal postorder akan mencetak urutan node sesuai dengan aturan postorder.
#3. Traversal postorder sering digunakan untuk menghapus node dari sebuah tree atau untuk mendapatkan representasi postfix dari ekspresi dalam sebuah binary expression tree.