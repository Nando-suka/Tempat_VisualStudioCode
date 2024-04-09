# Pembahasan Dicoding mengenai Ekspresi, Sekuensial, dan Control Flow
# Ekspresi merupakan suatu gabungan dari variabel, konstanta, maupun operator yang menghasilkan
# suatu nilai dalam operator tertentu

# Contoh Ekspresi dalam Python
y = 19
x = 8
z = x - y
print(z)

# Ekspresi juga dapat dilakukan untuk memanipulasi data yang ada
# Contoh manipulasi data dalam list (menggabungkan)
angka = [1,48,29,19,42,0,12]
alat = ["gunting","tang","sepatu","flashdisk"]
gabungan = angka + alat
print(gabungan)

# Contoh manipulasi data dalam list (menduplikasi)
angka2 = [2,4,2,1]
duplikasi = angka2 * 2
print(duplikasi)

x = 1960 
y = 901 
print(x % y)

# One Liner pada Python yang merupakan salah satu contoh dari penerapan sekuensial
x = 8
y = 9

x,y = y,x
print(x,y)

#  Sum Over Every Second List Value
lsit = [2,46,8,9,9]
jawaban = sum(lsit[::2])
print(jawaban)

# One Liner dengan kondisi statement
bakso = 20000
if bakso == 20000: print("Harga normal")

# Ternary operator di Python
hujan = True

print("Menggunakan Jas Hujan") if hujan else print("Tidak menggunakan Jas Hujan")

kehadiran = False
# Implementasi Ternary Tuple
""" Perlu diingat oleh Anda, ternary tuples sebaiknya dihindari terutama untuk 
kode dan klausa true/false yang kompleks. Komunitas Python sendiri menganggap
bahwa cara ternary tuples ini kurang "pythonic" atau "tidak Python banget!"
karena cukup membingungkan untuk meletakkan kondisi saat True atau False.
 """
Absen = ("Tidak Hadir !","Hadir") [kehadiran]
print(Absen)