# Membuat bubble sort dalam Python (by Suraj)
def bubblesot (list):
    m = len(list)

    # Melintasi semua larik elemen
    for i in range (m):
        swapperd = False

        # Elemen terakhir i sudah ada di elemen
        for j in range (0, m-i-1):

            # Melintasi array dari o ke variabel m dikurang - dan dikurang dengan 1
            # Tukar jika menemukan elemen ditemukan lebih besar
            # Kemudian elemen dilanjutkan
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
                swapped = True
        if swapped == False:
            break

# Driver code untuk menguji code
if __name__ == '__main__':
    list1 = [64, 34, 25, 12, 22, 11, 90]
    list2 = [23,434,45,132,4,65,7,8,56,86,4,234,54]
    bubblesot(list1)
    bubblesot(list2)

    print("Sorted Array: ")
    for i in range (len(list1)):
        print("%d" % list1[i], end=" ")

    print()
    for i in range (len(list2)):
        print("%d" % list2[i], end=" ")

print()

# Membuat bubble sort 2
def bubblesort (nums):
    n = len(nums)
    for i in range (n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

list2 = [90,34,542,54,3,24]
print(bubblesort(list2))

# Membuat bubble sort 3

def bubbleSort (angka):
    an = len(angka)
    for i in range(an):
        for j in range(an - i - 1):
            if angka[j] > angka[j+1]:
                angka[j], angka[j+1] = angka[j+1], angka[j]
    return angka

list3 = [4,30,23,42,19,49,58,63,23,42]
print(bubbleSort(list3))

angka = [1,2,3,4,5]
n = len(angka)
for i in range (n):
    for j in range (0, n-i-1):
        print(j, end=" ")

print()
angka2 = [10, 20, 30, 40, 50]
m = len(angka2)
for i in range(m):
    for j in range(0, m - i - 1):
        print(j, end=' ')

print()
for i in range (len(angka)):
    print(i, end=" ")
print()
for i in range (n):
    for j in range(0, i):
        print(j, end=" ")
print()
for i in range (n):
    for j in range (n-i):
        print(j, end=" ")
print()
for i in range (n):
    for j in range(n-i-1):
        print(j, end=' ')

# Bukankah keren implementasi dari virtual environment?
# Bisa menjalankan masing-masing kegunaan dari library secara terpisah.
# Tidak secara global
# Bagaimana ini masih banyak sekali yang harus saya pelajari dan saya harus benar-benar perhatikan
# errrorrrrrrr
