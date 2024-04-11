# Pembahasan Dicoding mengenai array dan pemrosesannya

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