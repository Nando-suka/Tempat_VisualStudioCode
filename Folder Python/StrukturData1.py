import numpy as np

array2 = [[23,25,18,20], [45,67,54,32], [10,29,9,17], [9,11,39,29]]
array3 = [[10,15,20,25], [13,26,39,52], [33,66,99,122], [100,200,300,400]]
#print(array)

# Menampilkkan data Umur
umur = [20,21,22,20,21,22,23,20,23]
print(umur.count(22)) # Menampilkan jumlah data umur 22
print(len(umur)) # Menampilkan jumlah umur
print(umur.index(21)) # Menamiplkan index umur 21
print(umur)

# Melakukan penampian 2 dimensi dengan perulangan
for rows in array2:
    for columns in rows:
        print(columns, end="")
        print()

# Menggunakan library numpy
vctr = np.array(array2)
print(vctr)
print("Vector dari array numpy:", vctr)

list2 = ["Melati", "Mawar", "Kamboja", "matahari"]
vctr2 = np.array(list2)
print("Nama-nama bunga:", vctr2)
