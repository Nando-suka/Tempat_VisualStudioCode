def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Target tidak ditemukan

# Contoh penggunaan:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [20,21,22,23,24,25,26,27,28,29,30]
target = 11
target2 = 23
result = binary_search(data, target)
result2 = binary_search(data2, target2)
print(len(data))
print(7 // 2)
print(f'Elemen {target} ditemukan di indeks {result}')
print(f'Elemen {target2} ditemukan di indeks {result2}')

# Memodifikasi dengan menambahkan hasil pertanyaan
print("-------------------------------")
tanya = int(input("Masukkan angka yang Anda ingin cari: "))
hasil = binary_search(data,tanya)
if hasil == -1:
    print("Maaf data Anda tidak ditemukan")
else:
    print("Data Anda: ", tanya, "telah berhasil ditemukan pada indeks ke", hasil)

