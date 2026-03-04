#====================================================#
#           Nama : Muhammad Haris
#           NIM : J0403251141
#           Prodi : Teknologi Rekayasa Perangkat Lunak B2
#
#
#Merge Sort (Ascending)
#
#=====================================================#

def merge_sort(data):

    if len(data) <= 1:
        return data

    # Divide : membagi data menjadi dua bagian (left dan right) secara 
    # rekursif hingga data hanya terdiri dari satu elemen atau kosong
    mid = len(data) // 2
    left = data[:mid]    #slicing untuk membagi data menjadi dua bagian  (bagian kiri)
    right = data[mid:]  #slicing untuk membagi data menjadi dua bagian (bagian kanan)

    #recursive call untuk membagi data hingga mencapai base case (data dengan satu elemen atau kosong)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):

    result=[]
    i = 0
    j = 0

    #Membandingkan elemen dari kedua bagian (kiri dan kanan)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan elemen jika masih ada yang tersisa dari salah satu bagian
    result.extend(left[i:])
    result.extend(right[j:])

    return result

data = [38, 27, 43, 3, 9, 82, 10]
print("Data sebelum diurutkan:", data)
print("Data setelah diurutkan:", merge_sort(data))