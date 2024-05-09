""" 
    1. Atribut:

    - daftar_buku: Daftar yang berisi objek-objek Buku.
       - saya buat menjadi daftar_buku = dfb
    - judul_perpustakaan: String yang berisi nama perpustakaan.
       - saya buat menjadi judulPerpus
    - jam_buka: String yang berisi jam buka perpustakaan.
       - saya buat menjadi jamPerpus

    2. Metode:
    - tambah_buku(buku): Menambahkan objek Buku ke daftar daftar_buku.
    - pinjam_buku(judul_buku): Mencari buku dengan judul yang diberikan, menandai status buku sebagai dipinjam, dan menghapus buku dari daftar daftar_buku.
    - kembalikan_buku(judul_buku): Mencari buku dengan judul yang diberikan, menandai status buku sebagai dikembalikan, dan menambahkan kembali buku ke daftar daftar_buku.
    - tampilkan_daftar_buku(): Menampilkan daftar semua buku yang tersedia di perpustakaan.
 """
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"  # Bisa diubah menjadi "Dipinjam" saat dipinjam

class Perpustakaan:
    def __init__(self, judul_perpustakaan, jam_buka):
        self.judul_perpustakaan = judul_perpustakaan
        self.jam_buka = jam_buka
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def pinjam_buku(self, judul_buku):
        for buku in self.daftar_buku:
            if buku.judul == judul_buku and buku.status == "Tersedia":
                buku.status = "Dipinjam"
                print(f"Buku '{judul_buku}' berhasil dipinjam.")
                return
        print(f"Buku '{judul_buku}' tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, judul_buku):
        for buku in self.daftar_buku:
            if buku.judul == judul_buku and buku.status == "Dipinjam":
                buku.status = "Tersedia"
                print(f"Buku '{judul_buku}' berhasil dikembalikan.")
                return
        print(f"Buku '{judul_buku}' tidak tercatat sebagai buku yang dipinjam.")

    def tampilkan_daftar_buku(self):
        if self.daftar_buku:
            print("Daftar Buku:")
            for buku in self.daftar_buku:
                print(f"- {buku.judul} oleh {buku.penulis}")
        else:
            print("Perpustakaan tidak memiliki buku.")

perpustakaan = Perpustakaan("Perpustakaan Gemar Membaca", "Senin-Jumat, 08:00-17:00 WIB")
buku1 = Buku("Bumi", "Andrea Hirata")
buku2 = Buku("Laskar Pelangi", "Andrea Hirata")
buku3 = Buku("Manusia Gagal", "Osamu Dazai")

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)
perpustakaan.pinjam_buku("Bumi")
perpustakaan.kembalikan_buku("Laskar Pelangi")
perpustakaan.kembalikan_buku("Bumi")
perpustakaan.tampilkan_daftar_buku()



