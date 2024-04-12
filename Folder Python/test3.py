# Penangan Kesalahan (Error Handling dan Exception) dalam Python dan
# Operasi pada List, Set, dan String
z = 0
try:
 print(1/z)
except ZeroDivisionError:
 print("Anda tidak bisa membagi angka dengan nol")

# Fungsi Set
kumpulan = set([2,3,2,2,5,35,6,6,7,834,65,78,9,5,2])
kumpulan_2 = [2,3,2,2,5,35,6,6,7,834,65,78,9,5,2]
print(kumpulan)
print(len(kumpulan))

# Fungsi Min dan Max
print(min(kumpulan),max(kumpulan))

# Fungsi count pada Python
print(kumpulan_2.count(2))

# Fungsi count pada tipe data string
klub = 'Chelsea Fc'
cari = 'e'
print(klub.count(cari))

# Operator in dan not in untuk mencari data dan menghasilkan keluaran boolean
kalimat = 'Benda itu jatuh entah kemana saat ku datang melihatnya'
print('Benda' in kalimat) # True
print('ini' in kalimat)
print('aku' not in kalimat)
print('melihatnya' not in kalimat)

# Fungsi sort
merek_laptop = ['dell','acer','asus','lenovo','hp','apple','axioo','avell']
merek_laptop.sort()
print(merek_laptop)