#====================================================#
#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 2 - Membuat Node Tree
#======================================================
#======================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#membuat sebuah node root 
root = Node("A")

#membuat child level 1
root.left = Node("B")  # node anak kiri root
root.right = Node("C")  # node anak kanan root

#membuat child level 2
root.left.left = Node("D")  # node anak kiri dari B
root.left.right = Node("E")  # node anak kanan dari B
root.right.left = Node("F")  # node anak kiri dari C
root.right.right = Node("G")  # node anak kanan dari C

#menampilkan isi node
print("Data pada root: ", root.data)
print("Child kiri root: ", root.left.data)
print("Child kanan root: ", root.right.data)
print("Child kiri dari B: ", root.left.left.data)
print("Child kanan dari B: ", root.left.right.data)
print("Child kiri dari C: ", root.right.left.data)
print("Child kanan dari C: ", root.right.right.data)

#Pembahasan :
#1. Node adalah struktur dasar dalam tree yang menyimpan data dan memiliki referensi ke node anak kiri dan kanan.
#2. Pada contoh di atas, kita membuat sebuah tree dengan root "A" dan dua child "B" dan "C". Kemudian, kita menambahkan child untuk "B" yaitu "D" dan "E", serta child untuk "C" yaitu "F" dan "G".
#3. Dengan menggunakan referensi left dan right, kita dapat mengakses data pada node anak dan menampilkan isi node sesuai dengan struktur tree yang telah dibuat.