#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#
#=====================================================#

# Materi Rekursi : Membuat Kombinasi PIN
# Recursive case  → fungsi terus memanggil dirinya untuk menambah digit
# Base case       → berhenti saat panjang PIN sudah sesuai target
#
#=====================================================#

# ILUSTRASI PROSES REKURSI:
# Setiap level menambahkan satu digit baru.
# Level 1: "" → "0", "1", "2"
# Level 2: masing-masing bercabang lagi menjadi 3 kemungkinan
# Level 3: setiap hasil kembali bercabang 3
# Level 4: proses bercabang tetap sama
# Level 5: saat panjang mencapai 5 digit, hasil langsung dicetak

def buat_pin(panjang, hasil=""):
    """
    panjang : target jumlah digit PIN
    hasil   : kombinasi sementara yang sedang dibangun
    """

    # BASE CASE → jika panjang hasil sudah sama dengan target
    # Maka kombinasi selesai dan ditampilkan
    if len(hasil) == panjang:
        print("Kode PIN:", hasil)
        return

    # RECURSIVE CASE →
    # Tambahkan setiap kemungkinan angka (0,1,2)
    # Lalu lanjutkan proses rekursi
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(5)  # Contoh: menghasilkan semua kombinasi 5 digit dari angka 0, 1, dan 2 (00000, 00001, ..., 22222)