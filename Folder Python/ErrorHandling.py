try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Tidak bisa dibagi dengan nol")
else:
    print("Hasil:",result)
finally:
    print("Block Excecuted.")

try:
    hasil = 20 / 0
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Hasil = ", hasil)


def multiply(a, b):
    return a * b
try:
    mungkin = multiply("2", 3)  # Mencoba memanggil fungsi multiply dengan string dan integer
except TypeError as e:
    print(f"TypeError: {e}")


    try:
        data1 = [1,2,3,4,5]
        indeks = len(data1)
        for i in range (0,indeks):
            print(i, end=" ")
    except IndexError:
        print("Error: Indeks tidak sesuai")


try:
    satu = int(input("A: "))
    dua =  int(input("B: "))
    jawaban = satu + dua
    print("Hasil:", jawaban)
except ValueError: # Ketika jawaban tidak sesua       
    print("Error: tipe data tidak sesuai")

try:
    tnya = input("Apakah nama ibukota Jepang?: ")
except KeyboardInterrupt:
    print("\nError: dibatalkan oleh keyboard")

try:
    numbers = [1, 2, 3]
    numbers.sort(reverse="True")
except TypeError as e:
    print(f"Error: {e}")

try:
    result = 10 / "2"
except TypeError as e:
    print(f"Error: Tipe data yang dimasukkan tidak cocok.")

try:
    lst = [1, 2, 3]
    result = lst[5] / 0 # Mengakses indeks yang salah dengan dibagi dengan nol
except IndexError as e:
    print(f"Indexerror: {e}")
except ZeroDivisionError as f:
    print(f"Error: {f}")


print("\n\n")
print("Ketika semua datang")
print("Ia pergi begitu saja")
print("Tak lepas aku melupakan diri nya")
print("Apakah aku sanggup melakukan ini semua?")
print("Melintasi ruang dan waktu")
print("Salah di bagian manakah aku?: ")
print("Akankaha ku dapat mencapai hal tersebut?")