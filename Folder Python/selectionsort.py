def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Anggap elemen pertama dari bagian yang tidak terurut sebagai elemen terkecil
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen terkecil yang ditemukan dengan elemen pertama dari bagian yang tidak terurut
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Contoh penggunaan
arr = [64, 25, 12, 22, 11]
print("Array sebelum diurutkan:", arr)
sorted_arr = selection_sort(arr)
print("Array setelah diurutkan:", sorted_arr)
