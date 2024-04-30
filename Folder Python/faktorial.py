# Fungsi Faktorial
def faktorial (n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
print(faktorial(5))

# Fungsi bilangan Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

# Fungsi penyelesaian perosalan tower hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Pindahkan piringan 1 dari tiang {source} ke tiang {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Pindahkan piringan {n} dari tiang {source} ke tiang {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

n = 3  
tower_of_hanoi(n, 'A', 'C', 'B') 

# Fungsi penyelesaian permutasi dengan penggunaan rekursif
def generate_permutations(elements):
    if len(elements) == 1:  # Basis kasus: jika hanya ada satu elemen, hanya ada satu permutasi
        return [elements]

    permutations = []  # Menyimpan semua permutasi
    for i in range(len(elements)):
        elem = elements[i]  # Elemen saat ini untuk dijadikan elemen pertama
        # Sisa elemen setelah elemen saat ini diambil
        rest_elems = elements[:i] + elements[i+1:]
        # Rekursif untuk mendapatkan permutasi dari sisa elemen
        for perm in generate_permutations(rest_elems):
            permutations.append([elem] + perm)

    return permutations

# Contoh pemanggilan fungsi
elements = [1, 2, 3]
perms = generate_permutations(elements)
for perm in perms:
    print(perm)

# Fungsi mengurai string menjadi karakter
def unravel_string(string):
    # Basis kasus: jika string kosong, kembalikan list kosong
    if not string:
        return []

    # Ambil karakter pertama sebagai elemen pertama dalam list
    first_char = string[0]
    
    # Rekursif untuk sisa string dan gabungkan hasilnya dengan karakter pertama
    return [first_char] + unravel_string(string[1:])

# Contoh pemanggilan fungsi
string = "Hello"
result = unravel_string(string)
print(result)



