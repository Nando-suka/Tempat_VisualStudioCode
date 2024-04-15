# Membuat Kelas Antrian
class antrian:
    def __init__(self,kode_antri):
        self.kode_antri = kode_antri # Atribut kode_antri
        self.next = None # Atribut next ?

# Membuat Kelas Linkedlist  
class Linkedlist:
    # Membuat Konstruktor "head"
    def __init__(self):
        self.head = None 

    # Membuat prosedur "MasukanAwal"
    def MasukanAwal (self,data):
        data_baru = antrian(data) # Membuat atribut berupa data_baru
        data_baru.next = self.head # Membuat atribut data baru selanjutnya menjadi sama dengan kepala
        self.head = data_baru  # Menginisialisasi bahwa method head sama dengan atribut data_baru

    # Membuat parameter "Keluaran"
    def keluaran(self):
        bagianMencetak = self.head # Membuat atribut bagianMencetak yang dijadikan kepala
        while bagianMencetak: # Membuat iterasi
          print(bagianMencetak.kode_antri,end=' ') # Mencetak atribut tersebut diikuti dengan objek kode
          bagianMencetak = bagianMencetak.next # Menyatakan bahwa atribut bagianMencetak digeser ke selanjutnya

    # Membuat hapus parameter awal
    def hapusAwal (self):
        self.head = self.head.next # Menghapus awal atribut kepala dengan digeser ke node yang kosong

    # Membuat metode pencarian
    def search (self,value):
        current = self.head # Membuat atribut current menjadi kepala 
        position = 0 # Menginisialisasi atribut position menjadi 0
        while current:
            if current.kode_antri == value:
                return f"Hasil '{value}' ditemukan pada indeks {position}"
            current = current.next
            position += 1
        return f"Hasil '{value}' tidak ditemukan dalam list "
        
# Proses Pemanggilan parameter
if __name__ == '__main__':
    Pemanggilan = Linkedlist()
    Pemanggilan.MasukanAwal('4')
    Pemanggilan.MasukanAwal('3')
    Pemanggilan.MasukanAwal('2')
    Pemanggilan.MasukanAwal('1')

    Pemanggilan.keluaran()

    print()
    print("Setelah keluaran: ")
    Pemanggilan.hapusAwal()
    Pemanggilan.keluaran()
    
    print()
    print(Pemanggilan.search('2'))
    print(Pemanggilan.search('6'))
    mencari2 = Pemanggilan.search('3')
    print(mencari2)
