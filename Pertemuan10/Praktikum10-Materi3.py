#====================================================#
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Prodi : Teknologi Rekayasa Perangkat Lunak B2
#====================================================#

#====================================================#
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
#====================================================#
# Rotasi kiri digunakan untuk memperbaiki BST yang
# condong ke kanan (right-skewed). Node kanan naik
# menjadi root baru, root lama turun ke kiri.
#
# Ilustrasi:
#   Sebelum:        Sesudah:
#     10               20
#       \             /  \
#        20    →    10   30
#          \
#           30
#====================================================#


# Class Node untuk menyimpan data BST
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node
        self.data  = data   # nilai pada node
        self.left  = None   # child kiri
        self.right = None   # child kanan


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


# Fungsi rotasi kiri untuk menyeimbangkan BST yang condong ke kanan
# Langkah-langkah:
#   1. Simpan y  = child kanan x  → calon root baru
#   2. Simpan T2 = child kiri  y  → subtree yang harus dipindah
#   3. y.left  = x   → x turun menjadi child kiri y
#   4. x.right = T2  → T2 pindah menjadi child kanan x
#   5. Return y sebagai root baru
def rotate_left(x):  # Fungsi rotasi kiri dengan parameter x sebagai node yang dirotasi
    # x adalah root lama yang akan dirotasi
    y  = x.right  # y adalah child kanan x (akan menjadi root baru)
    T2 = y.left   # T2 adalah subtree kiri y, disimpan sementara sebelum diputus

    # Proses rotasi dimulai
    y.left  = x   # x menjadi child kiri dari y (y naik menjadi parent)
    x.right = T2  # child kanan x diganti dengan T2 (subtree yang disimpan tadi)

    # y menjadi root baru setelah rotasi
    return y  # Return y sebagai root baru


# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang secara manual
# Struktur awal (right-skewed):
#   10
#     \
#      20
#        \
#         30
root = Node(10)            # Buat node root dengan nilai 10
root.right = Node(20)      # 20 masuk ke kanan 10
root.right.right = Node(30)  # 30 masuk ke kanan 20

print("Preorder sebelum rotasi kiri:")  # Label output sebelum rotasi
preorder(root)                          # Tampilkan preorder sebelum rotasi

print("\n\nStruktur sebelum rotasi kiri:")  # Label struktur sebelum rotasi
tampil_struktur(root)                       # Tampilkan visual tree sebelum rotasi

# Melakukan rotasi kiri pada root
# Node 20 naik jadi root baru, node 10 turun jadi child kiri
root = rotate_left(root)  # Panggil rotate_left, hasilnya jadi root baru

print("\nPreorder sesudah rotasi kiri:")  # Label output sesudah rotasi
preorder(root)                            # Tampilkan preorder sesudah rotasi

print("\n\nStruktur sesudah rotasi kiri:")  # Label struktur sesudah rotasi
tampil_struktur(root)                       # Tampilkan visual tree sesudah rotasi