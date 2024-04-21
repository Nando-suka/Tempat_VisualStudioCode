# Belajar Style Guide pada Python

# Penggunaan Trailing Commas
kelompok = [
    "Kelompok 1",
    "Kelompok 2",
]
print(kelompok)

# Anotasi fungsi
def luasPersegiPanjang (panjang: int = 2,lebar: int = None):
    luas = panjang * lebar
    return luas

luas_satu = luasPersegiPanjang(lebar= 10)
print(luas_satu)

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


