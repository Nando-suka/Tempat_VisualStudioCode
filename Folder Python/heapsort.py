# Membuat Algoritma Heap Sorting
def heap(arr, n, i):
    terbesar = i  # inisialisasi node terbesar sebagai root
    kiri = 2 * i + 1
    kanan = 2 * i + 2

    # Periksa apakah left child dari root ada dan lebih besar dari root
    if kiri < n and arr[kiri] > arr[terbesar]:
        terbesar = kiri

    # Periksa apakah right child dari root ada dan lebih besar dari root
    if kanan < n and arr[kanan] > arr[terbesar]:
        terbesar = kanan

    # Tukar root jika perlu 
    if terbesar != i :
        arr[i], arr[terbesar] = arr[terbesar], arr[i]

        # Heapify subtree yang berpengaruh
        heap(arr, n, terbesar)
    
def heapSort (arr):
    n = len(arr)

    # Membangun max heap
    for i in range (n // 2 - 1, -1, -1):
        heap(arr,n,i)

    # Ekstraksi elemen satu per satu dari heap
    for i in range (n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # Tukar root dengan elemen terakhir
        heap(arr, i, 0) # Panggil heap pada heap yang direduksi

    return arr

# Contoh penggunaan
list_angka = [12,11,13,5,6,7]
list_angka2 = [10,23,4,5,12,3]
print("Array sebelum di sorting: ", list_angka)
sortiran = heapSort(list_angka)
sortiran2 = heapSort(list_angka2)
print("Array setelah disortig: ", sortiran)
print("Array setelah disorting kedua: ", sortiran2)

