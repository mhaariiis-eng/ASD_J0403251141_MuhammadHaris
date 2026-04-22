#====================================================#
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Prodi : Teknologi Rekayasa Perangkat Lunak B2
#====================================================#


#====================================================
# Latihan 1 : BST (Binary Search Tree)
#====================================================
# BST adalah struktur data pohon biner dengan aturan:
#   - Nilai node KIRI  < nilai node induk
#   - Nilai node KANAN > nilai node induk
# Aturan ini memastikan data tersusun terurut di dalam tree.
#====================================================


# ====================================================
# CLASS NODE
# ====================================================
# Representasi satu simpul (node) dalam BST.
# Setiap node menyimpan sebuah nilai dan dua referensi
# ke child kiri dan child kanan.
# ====================================================
class Node:
    def __init__(self, data):
        self.data  = data   # nilai yang disimpan di node ini
        self.left  = None   # referensi ke child kiri  (awalnya kosong)
        self.right = None   # referensi ke child kanan (awalnya kosong)


# ====================================================
# FUNGSI INSERT
# ====================================================
# Menyisipkan nilai baru ke posisi yang tepat dalam BST.
# Menggunakan pendekatan REKURSIF:
#   - Jika posisi kosong (None) → buat node baru di sini
#   - Jika data < root          → sisipkan ke subtree KIRI
#   - Jika data > root          → sisipkan ke subtree KANAN
#   - Jika data == root         → abaikan (tidak ada duplikat)
# ====================================================
def insert(root, data):
    # Basis rekursi: posisi kosong → buat node baru
    if root is None:
        return Node(data)

    if data < root.data:
        # Data lebih kecil → telusuri ke subtree KIRI
        root.left = insert(root.left, data)
    elif data > root.data:
        # Data lebih besar → telusuri ke subtree KANAN
        root.right = insert(root.right, data)
    # Jika data == root.data, tidak ada aksi (duplikat diabaikan)

    return root  # kembalikan node dengan posisi child yang sudah diperbarui


# ====================================================
# MEMBANGUN BST
# ====================================================
# root dimulai dari None (tree kosong), lalu setiap
# elemen di data_list disisipkan satu per satu.
# Catatan: nilai 50 muncul dua kali → yang kedua diabaikan.
# ====================================================
root = None
data_list = [50, 30, 20, 40, 70, 60, 50, 80]

for data in data_list:
    root = insert(root, data)

# Struktur BST yang terbentuk:
#
#          50          ← root
#         /  \
#       30    70
#      /  \  /  \
#    20   40 60  80
#
print("BST Berhasil dibuat dengan data")


# ====================================================
# Latihan 2 : Traversal Inorder
# ====================================================
# Inorder mengunjungi node dengan urutan:
#   KIRI → ROOT → KANAN
#
# Sifat istimewa Inorder pada BST:
#   Hasilnya selalu terurut dari KECIL ke BESAR.
# ====================================================


# ====================================================
# FUNGSI INORDER
# ====================================================
# Mencetak semua nilai node BST secara terurut naik.
# Bekerja secara rekursif:
#   1. Kunjungi seluruh subtree KIRI terlebih dahulu
#   2. Cetak nilai node saat ini (ROOT)
#   3. Kunjungi seluruh subtree KANAN
# ====================================================
def inorder(root):
    if root is not None:
        inorder(root.left)          # 1. telusuri ke kiri dulu
        print(root.data, end=" ")   # 2. cetak nilai node ini
        inorder(root.right)         # 3. telusuri ke kanan


print("\nHasil Inorder: ")
inorder(root)
# Output yang diharapkan: 20 30 40 50 60 70 80  (urut naik)


# ====================================================
# Latihan 3 : Search di BST
# ====================================================
# Pencarian di BST memanfaatkan aturan BST sehingga
# setiap langkah membuang setengah dari sisa tree.
# Kompleksitas waktu rata-rata: O(log n)
# Kompleksitas waktu terburuk : O(n) — jika tree tidak seimbang
# ====================================================


# ====================================================
# FUNGSI SEARCH
# ====================================================
# Mencari nilai 'key' di dalam BST secara rekursif.
#
# Alur pencarian:
#   - Jika root kosong          → nilai tidak ada → return False
#   - Jika root.data == key     → nilai ditemukan → return True
#   - Jika key < root.data      → cari di subtree KIRI
#   - Jika key > root.data      → cari di subtree KANAN
#
# Parameter:
#   root (Node) : node yang sedang diperiksa
#   key  (int)  : nilai yang dicari
#
# Return:
#   True  → key ditemukan di BST
#   False → key tidak ada di BST
# ====================================================
def search(root, key):
    # Basis rekursi: tree habis ditelusuri, key tidak ditemukan
    if root is None:
        return False

    if root.data == key:
        # Nilai yang dicari ditemukan pada node ini
        return True
    elif key < root.data:
        # Key lebih kecil → lanjutkan pencarian ke KIRI
        return search(root.left, key)
    else:
        # Key lebih besar → lanjutkan pencarian ke KANAN
        return search(root.right, key)


# ====================================================
# UJI PENCARIAN
# ====================================================
key = 40  # nilai yang akan dicari di dalam BST

if search(root, key):
    print(f"\n{key} ditemukan di BST.")
else:
    print(f"\n{key} tidak ditemukan di BST.")