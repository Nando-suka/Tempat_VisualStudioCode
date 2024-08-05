daftar_angka = [3, 1, 52, 26, 38, 57, 9, 49]
ukuran = len(daftar_angka)
tengah = ukuran // 2


def kiriarray(arr):
    for i in range(tengah):
        tengah2 = tengah // 2
        for j in range(tengah2 - i):
            print(j, end=' ')
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


print(kiriarray(daftar_angka))
print()
for i in range(tengah, ukuran):
    print(daftar_angka[i], end=' ')

print()
