import numpy as np
from time import gmtime, strftime

# Program array
print("\t\tSelamat Datang\n")
daftar_angka = np.array([[10, 20, 30], [11, 21, 31], [12, 22, 32]])

print("Daftar Angka: ")
for i in daftar_angka:
    for j in i:
        print(j, end=' ')

indeks = 0
for i in daftar_angka:
    indeks = indeks + 1
    print()
    print("Urutan kolom nomor", indeks)
    for j in i:
        print(j, end=' ')

print('\n')
try:
    bertanya = input("Apakah Anda ingin melihat detail? [y/t]: ")
except KeyboardInterrupt:
    print("Error dari Keyboard")
else:
    if bertanya == 'y' or bertanya == 'Y':
        print("Angka paling besar: ", daftar_angka.max())
        print("Angka paling kecil: ", daftar_angka.min())
        print("Nilai rata-rata: ", daftar_angka.mean())
        print("Nilai pada baris 0 kolom 3:", daftar_angka.item(6))
        print()
        print("Nilai keseluruhan:", daftar_angka.sum())
    else:
        print("Terima kasih.")


# Eksplor numpy bre
daftar_nama = ["Fernando", "Aseo", "Yunita", "Erding"]
pengubah = daftar_nama
state = np.copy(pengubah)

print()
print(daftar_nama)
print(state)
state[1] = 'Aeseo'
print(state[1])

# np.copy tidak akan terubah saat ada data yang kita ubah
# Melalui reference
daftar_nama[0] = "Okuno"
print(daftar_nama[0] == pengubah[0], daftar_nama[0] == state[0])

# Eksplor numpy bre (2)
state2 = np.array(daftar_nama)
print(type(state2))
print()

daftar_angka2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def jawaban(n):
    salin = np.copy(n)
    return salin


try:
    print("Array:", daftar_nama)
    bertanya = int(input("Ketik 1 jika ingin menyalin array: "))
except ValueError as e:
    print("Error lu: Enggak sesuai sama tipe data nya cuk")
except KeyboardInterrupt:
    print("Error dari keyboard ini mah")
else:
    if bertanya == 1:
        salinan = jawaban(daftar_nama)
        print("Selamat berhasil disalin")
        print(salinan)
    else:
        print("Anda selesai.")


def fungsi(n, angka=10):
    an = n + angka
    return an


jika = fungsi(10)
print()
print(jika)

# Membuat fungsi dengan argumen boolean


def memastikan(n):
    if n == 0:
        return
    print(n, end=' ')
    memastikan(n - 1)


bertanya2 = int(input("Masukkan angka yang ingin diulang:"))
memastikan(bertanya2)

bertanya3 = input("Apakah Anda ingin melihat waktu saat ini?: ")

if bertanya3 == "y":
    print(strftime("%a,%d %b %Y %H:%M:%S +0000", gmtime()))
else:
    print("Baik Anda tidak ingin melihat waktu")


# And always remember who you are
# The greatest that make you always smil
# Please dom't spread hate and your hateful heart
# Get calm and focused on God
# Look at this recently world
# The world has showed the end is near
# so get ready for what will happen on the several next year
# Otherwise, Please ! Please ! Please !, hear me out
# Bring your time to be more near with god
# Don't forget to say God every day
# The world is outta nowhere will be end
# And you must defend an prepare
# So at the end you know about it
# Just say

array_angka = [1, 5, 10, 15, 20]
array_angka2 = [2, 4, 9, 14, 19]

total_array = array_angka +array_angka2
print(total_arrays)