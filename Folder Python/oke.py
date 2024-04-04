# Mencoba mengingat 3 pertemuan yang sudah diajarkan dalam Pemrograman Lanjut

print("-- Sistem Input Nilai --")
print("1. Tambah Nilai \n2. Lihat Nilai \n3. Keluar")

pilihan = int(input("Masukkan Pilihan : "))

if (pilihan == 1):
    print()
    nilai_2 = 5
    for i in range(1,3):
     print("Silakan Input Nilai\n- - - - - -")
     nilai = int(input("Masukkan Nilai = "))
     matkul = input("Masukkan Mata Kuliah = ")

     print("---------------------------------")
     print("Matakuliah " + matkul)
     if (nilai >= 90 and nilai <= 100):
         if (nilai >= 95):
             print("Nilai A+")
         else:
             print("Nilai A")
     elif (nilai >= 80 and nilai <= 89):
         if (nilai >= 85):
             print("Nilai B+")
         else:
            print("Nilai B")
     elif (nilai >= 70 and nilai <= 79):
         if (nilai >= 75):
             print("Nilai C+")
         else:
             print("Nilai C")
     elif (nilai >= 60 and nilai <= 69):
         if (nilai >= 65):
             print("Nilai D+")
         else:
             print("Nilai D")
     else:
         print("Nilai E")
     print("---------------------------------")

     bertanya = input('Apakah Anda ingin memasukkan data lagi ? [Y/N] : ')
     if (bertanya == "Y" or bertanya == "y"):
         print()
     elif (bertanya == "N" or bertanya == "n"):
         break
     else:
         print("Input salah silakan memasukkan kembali")

else: 
    if (pilihan == 2):
        print()
    else:
        if (pilihan == 3):
            print()
        else:
            print("Tidak ditemukan")
