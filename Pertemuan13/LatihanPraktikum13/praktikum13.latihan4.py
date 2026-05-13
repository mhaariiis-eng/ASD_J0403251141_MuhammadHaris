# ==========================================================
# Nama  : Muhammad Haris
# NIM   : J0403251141
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# Tujuan: Menentukan rute pemasangan kabel internet antar
#         gedung kampus dengan total biaya minimum menggunakan
#         algoritma Prim.
# ==========================================================

import heapq  # digunakan untuk priority queue pada algoritma Prim

# ----------------------------------------------------------
# Representasi weighted graph: jaringan antar gedung kampus
# Node  : GedungA, GedungB, GedungC, GedungD
# Edge  : hubungan antar gedung beserta biaya kabel (satuan juta)
# ----------------------------------------------------------
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Tampilkan semua koneksi yang tersedia
print("=" * 55)
print("Studi Kasus: Jaringan Kabel Internet Antar Gedung Kampus")
print("=" * 55)
print("\nDaftar semua kemungkinan koneksi kabel:")
print(f"  {'Koneksi':<30} {'Biaya (juta)'}")
print("  " + "-" * 40)
ditampilkan = set()
for gedung, tetangga in graph.items():
    for tujuan, biaya in tetangga.items():
        pasangan = tuple(sorted([gedung, tujuan]))
        if pasangan not in ditampilkan:
            print(f"  {gedung} - {tujuan:<20} {biaya}")
            ditampilkan.add(pasangan)


def prim(graph, start):
    """
    Mencari MST dengan algoritma Prim.
    Mulai dari 'start', pilih edge terkecil ke node yang belum
    terhubung, hingga seluruh node masuk ke dalam spanning tree.
    """
    visited = set([start])   # node yang sudah masuk ke MST
    heap = []                # priority queue menyimpan (bobot, dari, ke)

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))

    mst = []           # edge-edge terpilih dalam MST
    total_biaya = 0    # total biaya pemasangan kabel

    print(f"\nMembangun jaringan dari: '{start}'")
    print("-" * 55)

    while heap:
        biaya, dari_gedung, ke_gedung = heapq.heappop(heap)

        if ke_gedung not in visited:
            # Node belum terhubung → tambahkan ke MST
            visited.add(ke_gedung)
            mst.append((dari_gedung, ke_gedung, biaya))
            total_biaya += biaya
            print(f"  Pasang kabel: {dari_gedung} → {ke_gedung}  "
                  f"(biaya: {biaya} juta)  ✓")

            # Tambahkan edge-edge dari node baru ke heap
            for neighbor, w in graph[ke_gedung].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, ke_gedung, neighbor))

    return mst, total_biaya


# Jalankan algoritma Prim mulai dari GedungA
mst, total = prim(graph, 'GedungA')

# Tampilkan hasil rute kabel optimal
print("\n" + "=" * 55)
print("Hasil Jaringan Kabel dengan Biaya Minimum (MST Prim):")
print("=" * 55)
print(f"\n  {'Koneksi Kabel':<35} {'Biaya'}")
print("  " + "-" * 45)
for dari, ke, biaya in mst:
    print(f"  {dari} ↔ {ke:<22} {biaya} juta")
print("  " + "-" * 45)
print(f"  {'TOTAL BIAYA MINIMUM':<35} {total} juta")
print("=" * 55)

print(f"\nJumlah gedung    : {len(graph)}")
print(f"Jumlah kabel dipasang : {len(mst)} (= {len(graph)} gedung - 1)")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Algoritma apa yang digunakan?
#    Algoritma Prim. Dipilih karena graph ini termasuk dense
#    (setiap gedung terhubung ke banyak gedung lain), dan Prim
#    lebih efisien pada graph padat dibanding Kruskal.

# 2. Edge mana saja yang dipilih?
#    - GedungA → GedungC  (biaya 2 juta)
#    - GedungC → GedungD  (biaya 1 juta)
#    - GedungD → GedungB  (biaya 3 juta)
#    Total 3 koneksi untuk 4 gedung (N-1 = 3 edge).

# 3. Berapa total biaya minimum?
#    Total biaya = 2 + 1 + 3 = 6 juta rupiah.
#    Ini adalah biaya pemasangan kabel paling efisien yang tetap
#    menghubungkan seluruh gedung.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan SEMUA gedung (seluruh
#    node) dengan biaya TOTAL MINIMUM, tanpa perlu membentuk
#    koneksi berlebihan (cycle). MST menjamin bahwa setiap gedung
#    dapat berkomunikasi satu sama lain melalui jalur kabel yang
#    ada, dengan total panjang/biaya kabel yang paling hemat.
#    Koneksi redundan (cycle) hanya membuang biaya tanpa manfaat
#    tambahan karena konektivitas sudah terjamin.
