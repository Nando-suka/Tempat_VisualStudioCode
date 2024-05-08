# Membuat kelas bangun datar
class BangunDatar:
    def __init__ (self, nama, jumlah_sisi): # Konstruktor kelas
        self.nama = nama
        self.jumlah_sisi = jumlah_sisi

    def hitungKeliling (self): # Metode hitung Keliling
        pass

    def hitungLuas (self): # Metode hitung luas
        pass

# Membuat kelas persegi
class persegi (BangunDatar): # Mengambil inheritance (turunan) dari BangunDatar
    def __init__(self, nama, sisi): # Konstruktor kelas persegi
        super().__init__(nama,4) # mengisi parameter sesuai dengan konstruktor yang ada di BangunDatar
        self.sisi = sisi 

    def hitungKeliling(self): # Turunan metode abstrak dari kelas BangunDatar
        return 4 * self.sisi
    
    def hitungLuas(self): # Turunan metode abstrak hitungLuas dari kelas BangunDatar
        return self.sisi * self.sisi
    
# Membuat kelas persegi panjang
class persegiPanjang (BangunDatar): # Inheritance kelas BangunDatar
    def __init__(self, nama, panjang, lebar): # Konstruktor kelas
        super().__init__(nama,4) # Penegasan sisi kelas
        self.panjang = panjang
        self.lebar = lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar) # Metode abstrak hitungKeliling
    
    def hitungLuas(self):
        return self.panjang * self.lebar # Metode abstark hitungLuas
    
# Membuat kelas segitiga
class segitiga (BangunDatar): # Inheritance kelas BangunDatar
    def __init__(self, nama, alas, tinggi ): # Konstruktor kelas
        super().__init__(nama, 3) # Penegasan sisi kelas
        self.alas = alas
        self.tinggi = tinggi

    def hitungKeliling(self): # Melewatkan metode keliling segitiga
        pass

    def hitungLuas(self): # Metode abstrak hitungLuas
        return 0.5 * self.alas * self.tinggi
    
# Membuat kelas lingkaran
class lingkaran (BangunDatar): # Inheritance kelas BangunDatar
    def __init__(self, nama, jari_jari): # Konstruktor kelas
        super().__init__(nama,0) # Penegasan sisi kelas
        self.jari_jari = jari_jari

    def hitungKeliling(self): # Metode abstrak hitungKeliling
        return 2 * 3.1415 * self.jari_jari
    
    def hitungLuas(self): # Metode abstrak hitungLuas
        return 3.1415 * self.jari_jari * self.jari_jari
    
# Membuat kelas belah ketupat
class belahKetupat (BangunDatar): # Inheritance kelas BangunDatar
    def __init__(self, nama, sisi, diagonal1, diagonal2): # Konstruktor kelas
        super().__init__(nama,4) # Penegasan sisi kelas
        self.sisi = sisi
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def hitungKeliling(self): # Metode abstrak hitungKeliling
        return 4 * self.sisi
    
    def hitungLuas(self): # Metode abstrak hitungluas
        return 0.5 * self.diagonal1 * self.diagonal2

# Menampilkan penghitungan bangun data persegi
print("-"*15)
Persegi = persegi("Persegi", 10)
print(f"Nama: {Persegi.nama}")
print(f"Jumlah Sisi: {Persegi.jumlah_sisi}")
print(f"Sisi: {Persegi.sisi}")
print(f"Keliling: {Persegi.hitungKeliling()}")
print(f"Luas: {Persegi.hitungLuas()}")
print("-"*15)

# Menampilkan penghitungan bangun data persegi panjang
print()
print("-"*15)
PersegiPanjang = persegiPanjang("Persegi Panjang",10,20)
print(f"Nama: {PersegiPanjang.nama}")
print(f"Jumlah Sisi: {PersegiPanjang.jumlah_sisi}")
print(f"Panjang: {PersegiPanjang.panjang}")
print(f"Lebar: {PersegiPanjang.lebar}")
print(f"Keliling: {PersegiPanjang.hitungKeliling()}")
print(f"Luas: {PersegiPanjang.hitungLuas()}")
print("-"*15)

# Menampilkan penghitungan bangun data belah ketupat
print()
print("-"*15)
belahketupat = belahKetupat("Belah Ketupat", 4, 20, 50)
print(f"Nama: {belahketupat.nama}")
print(f"Jumlah Sisi: {belahketupat.jumlah_sisi}")
print(f"Sisi: {belahketupat.sisi}")
print(f"Diagonal 1: {belahketupat.diagonal1}")
print(f"Diagonal 2: {belahketupat.diagonal2}")
print(f"Keliling: {belahketupat.hitungKeliling()}")
print(f"Luas: {belahketupat.hitungLuas()}")
print("-"*15)