# AYO bangun sendiri bubble sort

def bubbleSort (arr):
    penentu = len(arr)
    for i in range(penentu):
        for j in range(penentu - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return  arr

daftar_angka = [50,40,30,24,23,41,14]
satu = bubbleSort(daftar_angka)
print(satu)

# Apkah tidak bisa variabel dari node tersebut diarahkan kepada variabel lain atau string, untuk mendapatkan
# implementasi dalam kehidupan sehari-hari.
# implementasi dari breadth first search sendiri lebih baik jika kita mendapatkan data yang diinginkan
# jangan menjadi hal yang buruk?
# buruk banget ini mah
# capek oi.....
# dengan yang seharusnya menjadi terpikirkan menjadi