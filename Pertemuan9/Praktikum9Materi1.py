#====================================================#
#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 1 - Membuat Node
#======================================================
# Insertion sort dengan tracing
#======================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#membuat root tree  
root = Node("A")

#menampilkan isi node
print("Data pada root: ", root.data) 
print("Data kiri root: ", root.left)  
print("Data kanan root: ", root.right)

#Pembahasan :
#1. Node adalah struktur dasar dalam tree yang menyimpan data dan memiliki referensi ke node anak kiri dan kanan.
#2. Pada contoh di atas, kita membuat sebuah node dengan data "A" dan menyet left dan right sebagai None, yang berarti node tersebut tidak memiliki anak.
#3. Node dapat digunakan sebagai dasar untuk membangun struktur tree yang lebih kompleks dengan menambahkan node anak ke kiri dan kanan sesuai kebutuhan.
