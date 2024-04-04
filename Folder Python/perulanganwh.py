count = 0

while (count < 9):
   print('The count is: ',count)
   count = count + 1

angka = [1,2,3,4,5]

# Contoh perulangan for sederhana
for x in angka:
   print(x)

# Contoh pengulangan for
buah = ["nanas","apel","jeruk"]
for makanan in buah:
   print(makanan)

# Contoh penggunaan nested loop
i = 2

while (i < 100):
   j = 2

   while(j <= (i/j)):
      if not (i % j): 
         break
      j = j + 1
      
   if (j > i/j): 
      print (i, " is prime")
      i = i + 1

print("Good bye!")

pertanyaan = input("Apakah jawaban Anda: ")
angka = 0

# Menggunakan while dalam python
# While seringkali dikenal dengan sebutan uncounted loop (Tidak terbatas)
while(pertanyaan == "Ya"):
    angka = angka + 1
    pertanyaan = input("Apakah jawaban Anda: ")
    if (pertanyaan == "Tidak" or pertanyaan == "t"):
        break

print(angka)
