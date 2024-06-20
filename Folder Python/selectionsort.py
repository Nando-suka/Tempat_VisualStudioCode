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

# Contoh penggunaan dengan menggunakan isi dari arr sebanyak 20 value.
arr2 = [1,2,3,4,5,102,32,312,4,52,10,21,7,73,235,4,64,7357,88,6]
print("Sebelum dilakukan sorting dengan selection sort", arr2)
sorted_arr2 = selection_sort(arr2)
print("Setelah diurutkan maka", sorted_arr2)

# Membuat selection sort untuk kedua kali
# Membuat fungsi selectionn_sort(. . .)
def selectionn_sort (list):
    for i in range (len(list)):
        minimal = i # membuat variabel minimal yang didasarkan pada perulangan i
        for j in range (i+1, len(list)): # diberikan perulangan bersarang yang menyatakan rentang awal dari i ditambah dengan 1 dan mencapai rentang akhir yakni panjang dari list tersebut
            if list[j] < list[minimal]:
                minimal = j # diberikan kondisi jika list dari indeks ke j kurang dari list dari indeks minimal
                            # indeks minimal berpindah ke j
        
        list[i], list[minimal] = list[minimal], list[i] # Menukarkan elemen jika memenuhi kondisi tersebut.
    
    return list # akan mengembalikan keseluruhan list jika sudah selesai

# Contoh penggunaan kedua
angka = [0,123,4,34,34,1,3,4,23,546,67,3,5,9,29]
print("Array sebelum diurutkan: ", angka)
diurut = selectionn_sort(angka)
print("Array setelah diurutkan: ", diurut)

# Daftar algoritma sorting yang sedang/sudah saya pelajari: bubble sort, selection sort
# melakukan algoritma terbaik untuk melakukan pengurutan data
# selain itu, algoritma ini bergantung pada kompleksitas waktu dari masing-masing algoritma sorting
# Kita menggunakan bubble sort ketika data yang diurutkan sedikit
# Sedangkan selection sort dapat digunakan ketika data yang ingin diurutkan banyak n "pangkat 2"
# Selain itu penggunaan dari proxmox sebagai server dapat menghalangi penggunaan dari waktu yang menyebar
# penting untuk mengingat selain dokumentasi perlu dilihat dari keutuhan kode tersebut, seperti kita dapat menggunakan variabel untuk menetapkan operasi tertentu

# menguji jika dalam indeks tersebut huruf
huruf = ['a','i','c','b']
diurut2 = selectionn_sort(huruf)
print(diurut2)
# Berhasil !!!, diurut juga ternyata
konoha = ['Hinata', 'Kiba', 'Shikamaru', 'Ino','Sakura', 'Tenten']
diurut3 = selectionn_sort(konoha)
print(diurut3)
# Berhasil juga !!
# Untuk yang kalimat selection sort ini melihat dari awalan huruf
