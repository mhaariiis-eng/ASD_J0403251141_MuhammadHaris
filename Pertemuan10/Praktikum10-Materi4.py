#====================================================#
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Prodi : Teknologi Rekayasa Perangkat Lunak B2
#====================================================#

#====================================================#
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
#====================================================#
# Rotasi kanan digunakan untuk memperbaiki BST yang
# condong ke kiri (left-skewed). Node kiri naik
# menjadi root baru, root lama turun ke kanan.
#
# Ilustrasi:
#   Sebelum:        Sesudah:
#     30               20
#    /                /  \
#   20       →      10   30
#  /
# 10
#====================================================#


# Class Node untuk menyimpan data BST
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node
        self.data  = data   # nilai pada node
        self.left  = None   # child kiri
        self.right = None   # child kanan


# Fungsi insert untuk menambahkan data ke dalam BST
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


# Fungsi preorder untuk melihat isi tree
# Urutan kunjungan: ROOT → KIRI → KANAN
def preorder(root):  # Fungsi traversal preorder (root, left, right)
    if root is not None:  # Cek apakah node tidak kosong
        print(root.data, end=" ")  # Cetak data node terlebih dahulu
        preorder(root.left)        # Rekursi ke subtree kiri
        preorder(root.right)       # Rekursi ke subtree kanan


# Fungsi untuk menampilkan struktur tree secara visual dengan indentasi
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi menampilkan tree dengan struktur hirarki
    if root is not None:  # Cek apakah node tidak kosong
        print("   " * level + f"{posisi}: {root.data}")  # Cetak node dengan indentasi sesuai level
        tampil_struktur(root.left,  level + 1, "L")  # Rekursi ke child kiri dengan level + 1
        tampil_struktur(root.right, level + 1, "R")  # Rekursi ke child kanan dengan level + 1


# Fungsi rotasi kanan untuk menyeimbangkan BST yang condong ke kiri
# Kebalikan dari rotasi kiri. Langkah-langkah:
#   1. Simpan x  = child kiri  y  → calon root baru
#   2. Simpan T2 = child kanan x  → subtree yang harus dipindah
#   3. x.right = y   → y turun menjadi child kanan x
#   4. y.left  = T2  → T2 pindah menjadi child kiri y
#   5. Return x sebagai root baru
def rotate_right(y):  # Fungsi rotasi kanan dengan parameter y sebagai node yang dirotasi
    # y adalah root lama yang akan dirotasi
    x  = y.left   # x adalah child kiri y (akan menjadi root baru)
    T2 = x.right  # T2 adalah subtree kanan x, disimpan sementara sebelum diputus

    # Proses rotasi dimulai
    x.right = y   # y menjadi child kanan dari x (x naik menjadi parent)
    y.left  = T2  # child kiri y diganti dengan T2 (subtree yang disimpan tadi)

    # x menjadi root baru setelah rotasi
    return x  # Return x sebagai root baru


# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang dari data berurutan turun
# Data [30, 20, 10] → semua node masuk ke kiri (left-skewed):
#   30 jadi root
#   20 < 30 → masuk kiri 30
#   10 < 20 → masuk kiri 20
root = None  # Inisialisasi root sebagai None
data_list = [30, 20, 10]  # list data berurutan turun → tree condong ke kiri

for data in data_list:       # Loop untuk setiap data dalam list
    root = insert(root, data)  # Insert data ke dalam BST

print("Preorder sebelum rotasi kanan:")  # Label output sebelum rotasi
preorder(root)                           # Tampilkan preorder sebelum rotasi

print("\n\nStruktur sebelum rotasi kanan:")  # Label struktur sebelum rotasi
tampil_struktur(root)                        # Tampilkan visual tree sebelum rotasi

# Melakukan rotasi kanan pada root
# Node 20 naik jadi root baru, node 30 turun jadi child kanan
root = rotate_right(root)  # Panggil rotate_right, hasilnya jadi root baru

print("\nPreorder sesudah rotasi kanan:")  # Label output sesudah rotasi
preorder(root)                             # Tampilkan preorder sesudah rotasi

print("\n\nStruktur sesudah rotasi kanan:")  # Label struktur sesudah rotasi
tampil_struktur(root)                        # Tampilkan visual tree sesudah rotasi