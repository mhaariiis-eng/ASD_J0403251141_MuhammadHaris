# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 2 - Implementasi Algoritma Kruskal
# Tujuan: Memahami cara kerja algoritma Kruskal dalam
#         membentuk Minimum Spanning Tree (MST) dengan
#         memilih edge berbobot terkecil secara global.
# ==========================================================

# Daftar edge: format (bobot, node1, node2)
# Graph: A-B=4, A-C=2, A-D=5, B-D=3, C-D=1
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Langkah 1: Urutkan semua edge berdasarkan bobot terkecil
# Ini adalah ciri khas Kruskal - bekerja secara global dari edge terkecil
edges.sort()

print("=" * 50)
print("Algoritma Kruskal - Minimum Spanning Tree")
print("=" * 50)

# Tampilkan urutan edge setelah diurutkan
print("\nUrutan edge setelah diurutkan (bobot terkecil dulu):")
print(f"{'Edge':<10} {'Bobot'}")
print("-" * 20)
for w, u, v in edges:
    print(f"  {u}-{v:<6}   {w}")

# Inisialisasi MST dan variabel bantu
mst = []           # menyimpan edge-edge yang terpilih masuk MST
total_weight = 0   # akumulasi total bobot MST

# Set untuk melacak node yang sudah terhubung dalam MST
# (pendekatan sederhana: node dianggap aman jika belum keduanya ada)
connected = set()

print("\nProses pemilihan edge:")
print("-" * 40)

# Langkah 2-6: Iterasi setiap edge (sudah terurut dari terkecil)
for weight, u, v in edges:
    # Langkah 3: Periksa apakah edge membentuk cycle
    # Pada pendekatan sederhana ini: edge aman jika salah satu
    # node belum ada di dalam set 'connected'
    if u not in connected or v not in connected:
        # Langkah 4: Tidak membentuk cycle → tambahkan ke MST
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  Pilih {u}-{v} (bobot {weight}) → DITERIMA ✓")
    else:
        # Langkah 5: Membentuk cycle → abaikan
        print(f"  Pilih {u}-{v} (bobot {weight}) → DITOLAK (cycle) ✗")

# Tampilkan hasil MST
print("\n" + "=" * 50)
print("Hasil Minimum Spanning Tree (Kruskal):")
print("=" * 50)
for u, v, w in mst:
    print(f"  {u} -- {v}  (bobot: {w})")
print(f"\nTotal bobot MST = {total_weight}")
print("=" * 50)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1 dipilih pertama kali, karena setelah
#    diurutkan ia memiliki bobot paling kecil di antara semua edge.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena strategi Kruskal adalah greedy: dengan selalu memilih
#    edge terkecil yang tersedia (dan tidak membentuk cycle),
#    dijamin hasilnya adalah spanning tree dengan total bobot
#    minimum. Ini terbukti secara matematis melalui sifat cut property.

# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST = 1 + 2 + 3 = 6
#    (dari edge C-D=1, A-C=2, B-D=3)

# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#    ketika giliran mereka diproses, semua node (A, B, C, D) sudah
#    masuk ke dalam set 'connected'. Menambahkan edge tersebut
#    akan membentuk cycle karena kedua endpoint-nya sudah terhubung.
