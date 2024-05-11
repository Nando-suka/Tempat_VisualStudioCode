class Laptop:
    # Konstruktor
    def __init__(self,merek,warna,jenis_ram):
        self.merek = merek
        self.warna = warna
        self.jenis_ram = jenis_ram

    def tambah_ram (self):
        pass

    def ganti_warna (self):
        pass
    
# Konsep Inheritance (Pewarisan)


Laptop1 = Laptop("Asus","Hitam","DDR4")
Laptop2 = Laptop("Asus","Abu-abu","DDR4")
Laptop3 = Laptop("Acer","Putih","DDR5")
print(Laptop1.merek,Laptop1.jenis_ram,Laptop1.warna)
print(Laptop2.merek,Laptop1.jenis_ram,Laptop1.warna)
print(Laptop3.merek,Laptop1.jenis_ram,Laptop1.warna)
