# Mengakses nilai variabel array
dataUmur = [35,23,20,19,11]
print(dataUmur)
print(dataUmur[0])
print(dataUmur[3])

print()

dataUmur2 = [[56,29,28,29,10],[1,5,6,7,8],[14,14,15,16,16]]
print(dataUmur2)
print(dataUmur2[2][1])

print()

# Menambahkan nilai ke dalam Array
dataUmur3 = [1,2,3,4,5,6]
dataUmur3.insert(2,2) # Parameter awal adalah letak, lalu parameter selanjutnya adalah nilai yang ingin ditambahkan
print(dataUmur3)
print(dataUmur3.insert(2,2))

# Menggunakan inputan untuk menambahkan array
n = int(input())
a = []
for i in range(n):
        a.append([int(j) for j in input().split()])
print(a)

print()

m = int(input("Masukkan jumlah baris: "))
n = int(input("Masukkan jumlah kolom: "))

print("Masukkan elemen array per baris, pisahkan dengan spasi:")
array_2d = [list(map(int, input().strip().split())) for i in range(m)]

print("\nArray 2 Dimensi yang Anda Masukkan:")
for row in array_2d:
    print(row)

count = 9

while (count < 9):
   print('The count is: ',count)
   count = count + 1

