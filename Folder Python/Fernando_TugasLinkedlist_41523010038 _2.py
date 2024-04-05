# Membuat Kelas Antrian
class antrian:
    def __init__(self,kode_antri):
        self.kode_antri = kode_antri
        self.next = None

# Membuat Kelas Linkedlist
class Linkedlist:
    # Membuat Konstruktor "head"
    def __init__(self):
        self.head = None

    # Membuat parameter "MasukanAwal"
    def MasukanAwal (self,data):
        data_baru = antrian(data)
        data_baru.next = self.head
        self.head = data_baru

    # Membuat parameter "Keluaran"
    def keluaran(self):
        bagianMencetak = self.head
        while bagianMencetak:
          print(bagianMencetak.kode_antri,end=' ')
          bagianMencetak = bagianMencetak.next

    def hapusAwal (self):
        self.head = self.head.next
        
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

# Iseng-isengan