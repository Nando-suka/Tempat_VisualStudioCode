# Belajar Object Oriented Programming
class Mobil:
    # Atribut 
    warna = 'Biru'

Mobil1 = Mobil()
Mobil1.warna = 'Kuning'
print(Mobil1.warna)

# Class baju
class baju:
    warna = 'Hijau'

baju1 = baju()
print(baju1.warna)
baju2 = baju()
print(baju2.warna)

baju.warna = 'Cokelat'
print(baju1.warna)
print(baju2.warna)

# Class Motor
class Motor:
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

Motor1 = Motor('Merah','Yamaha',160)
Motor2 = Motor('Hijau','Kawasaki',200)
print(Motor1.merek)
print(Motor2.kecepatan)

print(Motor1.warna)
print(Motor2.warna)

Motor1.warna = 'Hitam'
print(Motor1.warna)
print(Motor2.warna)
print()

# Membuat Konsep Dekorator pada Python
def my_decorator (func):
    def wrapper ():
        print('Sebelum dieksekusi')
        func()
        print('Setelah dieksekusi')
    return wrapper

@my_decorator
def say_hallo ():
    print('Hello World')

say_hallo()

# Membuat method dari objek
class mobil:
    def __init__(self,ban,merek,kecepatan):
        self.ban = ban
        self.merek = merek
        self.kecepatan = kecepatan


    def tambahKecepatan (self):
        self.kecepatan += 10

mobil11 = mobil('Dunlop','Honda',200)
print(mobil11.kecepatan)

#mobil11.tambahKecepatan() 
mobil.tambahKecepatan(mobil11)
print(mobil11.kecepatan)

# Membuat Method Static
class celana:
    def __init__ (self,merek2):
        self.merek2 = merek2

    @staticmethod
    def intro_celana ():
        print("Ini adalah metode dari kelas celana")

celana.intro_celana()
celana_1 = celana('Levis')
celana_1.intro_celana()

print( )
# Membuat Method Class (Metode dari kelas)
class bus:
    def __init__ (self,merek):
        self.merek = merek

    @classmethod
    def perkenalan_bus (cls):
        print('Ini adalah metode dari kelas Bus')

bus.perkenalan_bus()
bus_1 = bus("Mercedes Benz")
bus_1.perkenalan_bus()

print()
# Inheritance (Pewarisan)
class motor:
    def __init__ (self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambahKecepatan(self):
        self.kecepatan += 10

class motor_sport (motor):
    def turbo (self):
        self.kecepatan += 50
        
motor1 = motor('Hitam','Beat',90)
print(motor1.kecepatan)
motor_sport1 = motor_sport()
