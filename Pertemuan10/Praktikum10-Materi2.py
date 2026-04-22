#====================================================#
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Prodi : Teknologi Rekayasa Perangkat Lunak B2
#====================================================#

#====================================================#
# Latihan 4: Membuat BST yang Tidak Seimbang
#====================================================#
# BST bisa menjadi tidak seimbang jika data dimasukkan
# secara berurutan naik atau turun, sehingga semua node
# condong ke satu sisi (seperti linked list).
#====================================================#


# Class Node untuk menyimpan data BST
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node
        self.data = data      # nilai pada node
        self.left = None      # child kiri
        self.right = None     # child kanan


# Fungsi insert untuk BST
# Menyisipkan data ke posisi yang tepat secara rekursif:
#   - data < root → masuk ke subtree KIRI
#   - data > root → masuk ke subtree KANAN
#   - data = root → diabaikan (tidak ada duplikat)
def insert(root, data):  # Fungsi untuk menyisipkan data ke dalam BST
    # Jika root kosong, buat node baru
    if root is None:  # Cek apakah root kosong
        return Node(data)  # Jika kosong, return node baru

    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:  # Cek apakah data lebih kecil dari root
        root.left = insert(root.left, data)  # Masukkan ke subtree kiri

    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:  # Cek apakah data lebih besar dari root
        root.right = insert(root.right, data)  # Masukkan ke subtree kanan

    return root  # Return node root yang sudah diupdate


# Fungsi preorder untuk melihat bentuk tree
# Urutan kunjungan: ROOT → KIRI → KANAN
def preorder(root):  # Fungsi untuk traversal preorder
    if root is not None:  # Cek apakah node tidak kosong
        print(root.data, end=" ")  # Cetak data node
        preorder(root.left)   # Rekursi ke subtree kiri
        preorder(root.right)  # Rekursi ke subtree kanan


# Fungsi sederhana untuk menampilkan struktur tree
# Menggunakan indentasi untuk menunjukkan kedalaman (level) node.
# Semakin dalam level, semakin banyak spasi di depannya.
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi untuk menampilkan struktur tree secara visual
    if root is not None:  # Cek apakah node tidak kosong
        print("   " * level + f"{posisi}: {root.data}")  # Cetak node dengan indentasi
        tampil_struktur(root.left,  level + 1, "L")  # Rekursi untuk child kiri
        tampil_struktur(root.right, level + 1, "R")  # Rekursi untuk child kanan


# -----------------------------
# Program utama
# -----------------------------
root = None  # Inisialisasi root sebagai None

# Data dimasukkan berurutan naik → tree condong ke kanan (right-skewed)
# - 10 jadi root
# - 20 > 10 → masuk kanan 10
# - 30 > 20 → masuk kanan 20
# Struktur yang terbentuk:
#   10
#     \
#      20
#        \
#         30
data_list = [10, 20, 30]  # List data yang akan dimasukkan ke BST

for data in data_list:       # Loop untuk setiap data dalam list
    root = insert(root, data)  # Insert data ke dalam BST

print("Preorder BST:")  # Cetak label preorder
preorder(root)          # Panggil fungsi preorder

print("\n\nStruktur BST:")   # Cetak label struktur tree
tampil_struktur(root)        # Panggil fungsi tampil_struktur