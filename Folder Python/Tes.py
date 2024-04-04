print("Institut Teknologi Sepuluh November")
var = "Hello"
print(var)
print("Python"[4])
print("Python"[2:2])    
print("Python".find("Pyt"))
print("python/java/c++".split("/"))
print("8 Ball".title())
print("Statisktik".lower().count("a"))
print("vocational".capitalize())
print("Pyyhon"[-1*len("Python")-1:3])
a = 4
b = 6
c = "Municipality"
d = "pal"
print(len(c))
print(c.upper())
print(c[a:b] + c[b+4])
print(c.find(d))
print('M'+('m'*3) * 2 + '-')
Nomor_telpon = 234-5678
print("Nomor telpon saya adalah ",Nomor_telpon)
quote = "Saya Mahasiswa Informatika"
print(quote + ":" + "Mercu Buana")
usia= 19
print("Usia: ",usia)
film = "the great gatsby".title()[:10].rstrip()
print(film,len(film))

# Program memotong karakter sederhana
aku = "Fernando"
potong = aku.split('o')
print(potong)

# Program memotong karakter pertama
dia = "Maholi"
print(dia[1])

# Program soal ke 18
firstName = 'Thomas'
middleName = 'Alva'
lastName = 'Edison'
yearOfBirth = 1847
print(
    "Tahun Kelahiran",firstName,middleName,lastName,
    "adalah",yearOfBirth
    )

# Program soal ke 19
badai = int(input(
    "Slahkan masukkan jumlah detik antara petir dan badai:"
    ))

jarak_badai = float(badai / 5)
print(
    "== Laporan menyimpulkan bahwa jarak dari badai adalah", 
    jarak_badai
    )

# Program soal ke 20
""" Tulis Program untuk meminta nama tim baseball,jumlah pertandingan
yang dimenangkan, dan jumlah pertandingan yang hilang sebagai
input, lalu tampilkan nama tim dan persentase pertandingan yang
dimenangkan.
 """
# Input
tim_baseball = input("Masukkan nama tim: ")
jml_kemenangan = int(input("Masukkan jumlah kemenangan: "))
jml_kehilangan = int(input("Masukkan jumlah pertandingan yang hilang: "))

# Proses
presentase = float(jml_kemenangan / (jml_kemenangan+jml_kehilangan))

if (presentase == 1.0):
    presentase = int(100)

# Output
print("="*10,"Baseball","="*10)
print("="*3,tim_baseball)
print("="*3,"Presentase kemenangan : ",presentase,"%")

# Latihan menggunakan sep dan end
print("Departemen","Kebersihan","A",sep='-')