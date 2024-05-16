"""  1. Buatlah 2 contoh fungsi tanpa return values dengan satu dan lebih parameter
 2. Buatlah sebuah fungsi untuk menampilkan variabel nama dan NRP
 3. Buatlah sebuah fungsi untuk menghitung luas segitiga. Beri penamaan fungsi tersebut
    dengan nama fungsi luas_segitiga
 4. Buatlah sebuah fungsi untuk menghitung total harga yang harus dikeluarkan untuk biaya
    kos dengan ketentuan sebagai berikut. Beri nama fungsi Bayar_kos
      - Biaya kos = 850 ribu
      - Keterlambatan = 5 hari
      - Denda terlambat = 50 ribu/hari
 """

# 1 Parameter
def main (n):
    print(f"Hal0 {n} senang berkenalan denganmu")

main("Chinese")

# Lebih dari 1 parameter
def tambah (a,b,c):
    z = a + b + c
    print("-------------------------------------")
    print()
    print("Hasil dari pertambahan ketiga bilangan adalah ", z)

tambah(10,20,20)

print()
# Jawaban soal nomor 2
def display (a, b):
    print()
    print("-"*5,"Tampilan Informasi","-"*5)
    print("Nama = ",a.capitalize())
    print("NRP  = ", b)

print("-"*5,"Informasi","-"*5)
bertanya1 = input("Silakan masukkan Nama Anda: ")
bertanya2 = input("Silakan masukkan NRP Anda: ")
display(bertanya1,bertanya2) # Menampilkan output

# Jawaban soal nomor 3
def luas_segitiga (a,t):
    hasil = 0.5 * a * t
    print("Luas segitiga adalah", hasil)

print()
print("--- Luas Segitiga ---")
bertanya3 = int(input("Silakan masukkan alas segitiga = "))
bertanya4 = int(input("Silakan masukkan tinggi segitiga = "))

luas_segitiga(bertanya3,bertanya4)

# Jawaban soal nomor 4
def bayar_kos ():
    BIAYA_KOS = 850000
    DENDA = 50000
    Total_pembiayaan_denda = BIAYA_KOS + (DENDA * 5) 
    print("----------------------------")
    print("\tBiaya Kos")
    print("Biaya Kos        = Rp850.0000,00")
    print("Keterlambatan    = 5 hari")
    print("Denda terlambat  = 50 ribu/hari")
    print("Total pembiayaan =", Total_pembiayaan_denda)

bayar_kos()

