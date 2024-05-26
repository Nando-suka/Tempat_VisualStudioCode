# Operasi input kedalam list
kosong = []
bertanya = input("Apakah Anda ingin memasukkan data?: ")
while bertanya != "tidak" or bertanya != "t":
    masukkan = input("Silahkan masukkan nama pemain: ")
    kosong.append(masukkan)
    bertanya = input("Apakah Anda ingin memasukkan data?: ")
    if bertanya == "t":
        break

print(kosong)

# Implementasi array
import array

arr = array.array('i')
arr = array.array('b')
arr = array.array('f')

# Static Array (Compile-time)
arr = array.array('i',[1,2,3,4,5])
print(arr)

# Python implementation insert element
def insertElement (arr, n, x, pos):
    # menggeser elemen ke kanan
    # yang mana ada di bagian kanan
    for i in range (n-1, pos-1, -1):
        arr[i+1] = arr [i]
    
    arr[pos] = x

insertElement([10,20,30], 2, 1, 2)
