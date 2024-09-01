# Pembahasan Dicoding mengenai array dan pemrosesannya serta Matriks
import numpy as np
import sys
# Mendefinisikan Array
nama_var = [1,2,3,4,5]
print(nama_var)

# Mendefinisikan nilai Array dengan nilai default
nilai = [0 for i in range (1,10)]
print(nilai)

# Mengubah nilai default dengan nilai baru
nilai_baru = [0 for i in range(1,10)]

for i in range (9):
    nilai_baru [i] = i
print(nilai_baru)

# Mengubah nilai default dengan nilai baru (2)
nilai_baru2 = [1 for i in range(0, 10)]
ukuran = len(nilai_baru2)
for i in range(ukuran):
    nilai_baru2[i] = i
print(nilai_baru2)
# Mengubah nilai default dengan nilai baru (memakai string)
nama = 'Fernando'
nilai_baru_2 = [0 for i in nama]
print(nilai_baru_2)

for i in range(8):
     nilai_baru_2 [i] = nama
print(nilai_baru_2)


# Pemrosesan sekuensial dengan menggunakan array
nilai2 = [5,10,15,20,25]
print(len(nilai2))

for i in range(len(nilai2)):
    elemen_saatini = nilai2 [i]
    indeks_selanjutnya = i + 1

    if indeks_selanjutnya < len(nilai2):
        elemen_selanjutnya = nilai2[indeks_selanjutnya]
    else:
        elemen_selanjutnya = None

    print(f'Elemen saat ini: {elemen_saatini}, Elemen selanjutnya: {elemen_selanjutnya}')

print()

# Pemrosesan sekuensial menggunakan array (2)
buah = ['Mangga','Pisang','Apel','Melon','Rambutan']
print(len(buah))

for i in range(len(buah)):
    elemen_saatini_2 = buah [i]
    indeks_selanjutnya_2 = i + 1

    if indeks_selanjutnya_2 < len(buah):
        elemen_selanjutnya_2 = buah[indeks_selanjutnya_2]
    else:
        elemen_selanjutnya_2 = None

    print(f'Elemen saat ini: {elemen_saatini_2}, Elemen Seanjutnya: {elemen_selanjutnya_2}')
print()

# Implementasi Matriks menggunakan Python
matriks = [ [1,2,3], [4,5,6], [7,8,9,10]]
print(matriks)

matriks_2 = np.array([[1,2,3],[4,5,6]])
print(matriks_2)

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(matriks)*len(matriks))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", matriks_2.size*matriks_2.itemsize)

# Matriks menggunakan for nested beserta list comprehension
matriks_3 = [[0 for i in range(4)] for j in range(3)]
print(matriks_3)
print(matriks[1][2])

# Membuat matriks 2 x 2
matriks_4 = [[5,0],[1,-2]]
def_mat = [[0 for j in range(2)] for i in range (2)]

for i in range(len(matriks_4)):
    for j in range(len(matriks_4[0])):
        def_mat[i][j] = matriks_4[i][j] * 2

print(def_mat)
print(len(matriks_4[0]))

# membuat matriks dengan numpy
matriks_5 = np.array([[5,0],[1, -2]])
hasil = matriks_5 * 5
print(hasil)

# Membuat Parmeter
def film (a):
    print("Film " + a + " sangat seru")

film("Forget Me Not")
film("Drive My Car")
film("Joker")