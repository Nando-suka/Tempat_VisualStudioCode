class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies

# Contoh 1 turunan kepada hewan Anjing
class Anjing (Hewan):
    def __init__(self, nama, spesies, ras):
        super().__init__(nama, spesies)
        self.ras = ras

    def display (self):
        print(self.nama,self.spesies,self.ras)

# Contoh 2 turunan kepada hewan Kucing
class Kucing (Hewan):
    def __init__(self, nama, spesies, bulu):
        super().__init__(nama, spesies)
        self.bulu = bulu

    def display (self):
        print(self.nama,self.spesies,self.bulu)

# Contoh 3 turunan kepada hewan harimau
class harimau (Hewan):
    def __init__(self, nama, spesies, lokasi):
        super().__init__(nama, spesies) 
        self.lokasi = lokasi

    def display (self):
        print(self.nama,self.spesies,self.lokasi)

hewan1 = Anjing("Anjing","Akita","Anjing Pekerja")
hewan2 = Anjing("Anjing","Dalmasia","Anjing Rumah")
hewan3 = Kucing("Kucing","Siam","Cokelat")
hewan4 = Kucing("Kucing", "Persia","Putih")
hewan5 = harimau("Harimau", "Sumatera", "Indonesia")
print(hewan1.display())
print(hewan2.display())
print(hewan3.display())
print(hewan4.display())
print(hewan5.display())

# Pewarisan ke 2
