#Nama : Muhammad Haris
#NIM : J0403251141
#Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
# Latihan 6 - Membuat Struktur Organisasi Perusahaan 
#======================================================
#======================================================

#Class node adalah dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan data pada node
        self.left = None  # node anak kiri
        self.right = None  # node anak kanan

#membuat tree untuk struktur organisasi perusahaan
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")

#menampilkan struktur organisasi perusahaan
def print_organization(node, level=0):
    if node is not None:
        print(" " * (level * 4) + node.data)  # Indentasi berdasarkan level
        print_organization(node.left, level + 1)  # Kunjungi subtree kiri
        print_organization(node.right, level + 1)  # Kunjungi subtree kanan

print("Struktur Organisasi Perusahaan:")
print_organization(root)

#Pembahasan :
#1. Dalam contoh di atas, kita membuat sebuah tree yang merepresentasikan struktur organisasi perusahaan dengan "Direktur" sebagai root, "Manajer A" dan "Manajer B" sebagai child level 1, dan "Staff 1", "Staff 2", dan "Staff 3" sebagai child level 2.
#2. Fungsi print_organization digunakan untuk menampilkan struktur organisasi dengan indentasi yang sesuai berdasarkan level dalam tree, sehingga memudahkan untuk melihat hierarki dalam organisasi.
#3. Struktur tree sangat berguna untuk merepresentasikan hubungan hierarkis seperti dalam organisasi, di mana setiap node dapat memiliki beberapa child yang merepresentasikan posisi atau peran dalam perusahaan.