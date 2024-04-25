# Dicoding Transformasi angka,karakter, dan string

# Membuat keseluruhan nilai dalam string menjadi kapital
ayo = "ayo"
print(ayo.upper())

# Membuat keseluruhan nilai dalam string menjadi kapital
perkataan = "After all i do for you"
print(perkataan.upper())

nama_lengkap = ["Fernando","Gallagher","Maholi","Tumanggor","Felix","Owen"]
for i in nama_lengkap:
    print(i.upper(), end=" ")

print()
index = 0
while index < 10:
    print(index, end=" ")
    index += 1

# Membuat Keseluruhan nilai dalam string menjadi huruf kecil
ayo2 = "AYO"
print(ayo2.lower())

ayo3 = "FERNANDO".lower()
print(ayo3)

nama = "FERNANDO DAN MAHOLI TUMANGGOR"
print(nama.lower())

kota = 'JAKARTA BARAT'
print(kota.lower())
"""  Metode untuk menghapus whitespace dan kata yang tidak diinginkan
 dalam string dengan rata kanan
 """
ayo3 = "ayo     kita"
print("ayo    kita".rstrip())

"""  lstrip() memiliki metode yang sama dengan rstrip. Namun, lstrip ()
 digunakan untuk menghapus bagian kiri
 """

"""  strip() memiliki metode yang sama dengan rstrip dan lstrip. Namun, lstrip ()
 digunakan untuk menghapus bagian kiri dan kanan (keseluruhan bagian)
 """
ayo4 = "AyoayoayoayoayoayoAyobisa"
print(ayo4.strip("Ayo"))

# Menggunakan startswith untuk menemukan suatu kata pada awal kalimat
ayo5 = "Mari pergi ke hutan"
print(ayo5.startswith("Mari"))

# Menggunakan startswith untuk mengembalikan false 
ayo51 = "Aku melihatnya pergi"
print(ayo51.startswith("Dia"))

# Menggunakan endswith untuk menemukan suatu kata pada akhir string
ayo6 = 'Dia ingin belajar Cloud Computing'
print(ayo6.endswith('Cloud'))
print(ayo6.endswith("Computing"))
# Menggunakan .join() untuk menggabungkan atau memisahkan string 
print(" ".join(["Ayo","Indonesia"]))
print(" Menyala ".join(["Api","Air","Dia",""]))

# Metode .split() untuk memisahkan string menjadi list
ayo7 = "aku menjadi semangat dengan belajar sesuai passion"
print(ayo7.split())

# Metode .split() untuk memisahkan string menjadi list (2)
nama_merek_laptop = "Acer Asus HP Dell Lenovo Axioo Avell Msi "
dipisah = nama_merek_laptop.split()
print(dipisah[1])
print(dipisah)

# Metode untuk mengganti string selanjutnya dapat menggunakan tag .replace()
ayo8 = "Maholi sekolah di Smk Jakarta Satu"
print(ayo8.replace("sekolah","bersekolah"))

# Metode untuk memeriksa string apakah nilai yang terdapat pada string adalah huruf kapital
ayo9 = "AYOBERANINIKRI"
print(ayo9.isupper())

# Metode untuk mengecek apakah nilai yang ada pada string adalah huruf kecil semua
ayoo1 = "ayokitaPergi"
print(ayoo1.islower())

"""  Metode untuk mengecek apakah nilai yang ada pada string hanya huruf, hanya angka,
 maupun keduanya """
ayoo2 = "ColePalmer20"
ayoo3 = ' '
print(ayoo2.isalnum(),ayoo3.isalnum())

# isdecimal digunakan jika hanya angka/numerik yang terdapat di variabel
ayoo4 = '123'
print(ayoo4.isdecimal())

""" Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, 
seperti spasi, tab, newline, atau karakter whitespace lainnya. """
ayoo5 = "Fernando Datang"
print(ayoo5.isspace(),ayoo3.isspace())

# istitle akan mengembalikan true apabila setiap kata diikuti dengan huruf kapital
ayoo6 = 'Manusia Gagal'
print(ayoo6.istitle())

# zfill adalah metode formatting yang akan menambahkan nilai 0 didepan sebuah string
teks = 'Code'
teks_dua = 'Palmer'
tambah_angka = teks.zfill(5)
tambah_angka_dua = teks_dua.zfill(7)
print(tambah_angka_dua)
print(tambah_angka)

# rjust dapat membuat string menjadi rata kanan
print("Fernando".rjust(15))

# ljust dapat membuat string menjadi rata kiri
print("       Kini".ljust(12))

# center menjadikan teks rata tengah
ayoo7 = 'Judul'
print(ayoo7.center(10,'-'))

# Python menyediakan cara untuk mencetak string secara asli/murni dengan raw
print(r'Fernando\tTumanggor')

print(dict([['name','Dicoding'],['age',17]]))
print(dict([['Nama',"Fernando"], ['umur', 19]]))