# Ini pembuatan kelas
class Mobil:
    # Ini pembuatan atribut untuk mobil
    def __init__(self,merek,warna,kecepatan):
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan

    def tambahKecepatan (self):
        self.kecepatan += 10


# Proses Pemanggilan kelas
Mobil1 = Mobil("Toyota","Hitam",100)
print(Mobil1)
print(Mobil1.kecepatan)
Mobil1.tambahKecepatan()
print(Mobil1.kecepatan)

# Belajar memahami konsep private dan public 
class Diary:
    def __init__(self, title):
        self.title = title
        self._entries = []

    def addentry (self, entry):
        self._entries.append(entry)

    def _lastentri (self):
        return self._entries[-1]
    
# Proses pemanggilan kelas diary
catatan = Diary("Menambahkan judul")
catatan.addentry("Ini hari yang baik.")
print("Catatan ini diperlihatkan ...",catatan.title)

# Belajar menerapkan enkapsulasi pada python
class tugas:
    def __init__(self):
        self._rahasia = "Fernando mencintai seseorang"

    def __privateMessages (self):
        print("Ini Pesan Rahasia")

task1 = tugas()
task1.__privateMessages()