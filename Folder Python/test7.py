# Belajar Style Guide pada Python

# Penggunaan Trailing Commas
kelompok = [
    "Kelompok 1",
    "Kelompok 2",
]
print(kelompok)

nama_idola = [
    "Hoshino",
    "Ruby"
]
print(nama_idola)


# Anotasi fungsi
def luasPersegiPanjang (panjang: int = 2,lebar: int = None):
    luas = panjang * lebar
    return luas

luas_satu = luasPersegiPanjang(lebar= 10)
print(luas_satu)

# Anotasi Fungsi yang kedua
def kelilingpersegi(jumlah: int = 4, sisi: int = None):
    keliling = jumlah * sisi
    return  keliling

luaskeliliingPersegi = kelilingpersegi(sisi=8)
print(luaskeliliingPersegi)


# Tanpa Anotasi Fungsi
def luasSegitiga (alas=None, tinggi=None, tambahan=2):
    luas = 0.5*alas*tinggi*tambahan
    return luas

luasSegitiga_satu = luasSegitiga(10,20)
print(luasSegitiga_satu)    

# Penggunaan nama pada exception
class DivideByZeroError (Exception):
    def __init__(self, message="Division By Zero Is Not Allowed "):
        super().__init__(message)

def pembagian(a,b):
    if b == 0:
        raise DivideByZeroError("Tidak bisa dibagi dengan 0")
    return a / b

try:
    pembagian(2,0)
except DivideByZeroError as w:
    print(f"Error {w}")

# Penggunaan error input pada exception
class NegatifInputError (Exception):
    def __init__(self, pesan="Input tidak boleh menggunakan angkan negatif"):
        super().__init__(pesan)

def user_input (a):
    if a < 0:
       raise NegatifInputError("Input tidak boleh negatif")
    return a

try:
    masukkan = int(input("Silahkan masukkan nomor: "))
    user_input(masukkan)
except NegatifInputError as w:
    print(f"Error {w}")

# Persiapan penulisan kode untuk penggunaan private python
class Myclass:
    def __init__ (self):
        self._private_var = 42
        self._secret_list = [1,2,3]

    def _private_method (self):
        print("Ini adalah method non publik")

    def public_method (self):
        print("Ini adalah metode publik")
        self._private_method()

class mySecondClass:
    def __init__(self):
        self._rahasia_var = 12
        self._rahasia_list = [5,10,15]

    def _rahasia_method (self):
        print("Ini adalah method non publik")

    def publik_method (self):
        print("Ini adalah metode publik")
        self._rahasia_method()