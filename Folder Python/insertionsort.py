# Membuat insertion algorithm
def insertion(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a


daftar_angka = [31, 41, 59, 26, 41, 58]
hasil = insertion(daftar_angka)
print(hasil)


# Hasil jumlah keseluruhan pada Array
def sumarrray(a):
    jumlah = 0
    n = len(a)
    for i in range(0, n):
        jumlah = jumlah + a[i]
    return jumlah


tambah = sumarrray(daftar_angka)
print(tambah)

# For example in the real world of implementation of random maachine state
# seperti contoh pada kenyataan pada penulisan mesin secara tepat waktu
# that such an interest to the another example that you can run
# adding the receipt will be so good
# The viewpoint is keeping with the RAM model,and it also reflect on another base prgramming
# In order to ease our analysis of the Insertion Sort procedure, we used some simplifying abstractions
# We can now use the merge procedure as a subroutine
