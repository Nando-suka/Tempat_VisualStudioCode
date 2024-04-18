# Belajar Subprogram dalam Python
def hitung(kiri,kanan):
    z = kiri + kanan
    return z

# Ini termasuk pemanggilan dengan cara keyword argument
menghitung = hitung(1,9)
print(menghitung)

# Metode ini adalah pemanggilan fungsi menggunakan positional argumen
menghitung_dua = hitung(kanan = 5, kiri = 10)
print(menghitung_dua)

# Membuat fungsi
# Positional-or-Keyword
def pesanan (nama,barang,konfirmasi):
    return "Halo " + nama + " Pesanan "+ barang + " akan sampai " + konfirmasi 

konsumen1 = pesanan("Fernando","Flashdisk","segera")
print(konsumen1)

konsumen2 = pesanan(barang="baju",nama="Minka",konfirmasi="besok")
print(konsumen2)

# Parameter Postion Only
def pengurangan (x,y,/):
    return x - y

print(pengurangan(5,2))
#print(pengurangan(x = 8, y = 10)) akan menghasilkan type error 

# Parameter Keyword Only
def salam (*, nama, pesan):
    return "Halo " + nama + "! " + pesan

print(salam(nama="Maholi",pesan="Jangan tidur larut malam!"))

# Variadic Positional Parameter 
def hitung_total (*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1,2,3))
print(hitung_total(5,10,15))

# Variadic Keyword Argument
def cetak_info (**kwargs):
    info=""
    for key, value in kwargs.items():
        info += key + ':' + value + ", "
    return info

print(cetak_info(
    nama="Dicoding", usia="17", 
    pekerjaan="Python Programmer", tempat_lahir="Bandung", lulusan = "ITS"
    ))

# Penggunaan Lambda dalam Python
Mencari_luas_segitiga = lambda alas, tinggi: 0.5 * alas * tinggi
print(Mencari_luas_segitiga(10,5))

mencari_luas_persegi = lambda panjang, lebar: 2 * 4
print(mencari_luas_persegi(2,3))

pertambahan = lambda a,b,c,d: a + b + c + d
print(pertambahan(1,2,3,4))

#  Variabel Global dan Lokal
a = 10

def add(b):
    jumlah = a - b
    return jumlah

ttp = add(20)
print(ttp)

# Variabel Lokal dalam Python
def pertambahan (a,b):
    lokal = 10
    hasil = a + b - lokal
    return hasil

ttp2 = pertambahan(5,6)
print(ttp2)

"""  Dalam Python fungsi itu adalah first class object sehingga fungsi dapat dijadikan sebagai
argumen ataupun sebagai pass parameter. properties yang terdapat dalam fungsi Python:
1. Sebuah fungsi adalah sebuah instance dalam type objek
2. Kamu dapat memasukkan fungsi ke dalam variabel
3. kamu dapat pass sebuah fungsi sebagai parameter ke fungsi yang lain
4. kamu dapat mengembalikan fungsi dari fungsi
5. kamu dapat memasukkan mereka ke dalam struktur data, seperti hash tables, list, dan lain-lain
 """