# Dengan Menggunakan for
for i in range(1,4):
    for j in range(1,4):
        print(f"Nilai i: {i}, Nilai J: {j}")

# Dengan Menggunakan While
i = 1
while i < 4:
    j = i
    while j < 4:
        print(f"Nilai i: {i}, Nilai J: {j}")
        j += 1
    i += 1

# Dengan Menggunakan do while dan break
i = 1
while True:
    print(f"Nilai i: {i}")
    i += 1
    if i > 3:
        break

# Melakukan perulangan for untuk membentuk segitiga siku-siku
for i in range(1,6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Melakukan perulangan while untuk membentuk segitiga siku-siku
i = 1
while i < 6:
    j = 1
    while j < i + 1:
        print("*", end="")
        j += 1
    print()
    i += 1

# Melakukan perulangan dengan do-while untuk membentuk segitiga siku-siku
i = 1
while True:
    j = 1
    while j < i + 1:
        print("*", end="")
        j += 1
    print()
    i += 1
    if i > 5:
        break

# Melakukan perulangan for untuk membuat faktorial
bilangan = 5
faktorial = 1

for i in range(1, bilangan + 1):
    faktorial *= i
print(f"Faktorial dari {bilangan} adalah: {faktorial}")

# Melakukan perulangan while untuk membuat faktorial
bilangan = 5
faktorial = 1
i = 1
while i <= bilangan:
    faktorial *= i
    i += 1
print(f"Faktorial dari {bilangan} adalah: {faktorial}")

# Melakukan perulangan do-while untuk membuat faktorial
bilangan = 5
faktorial = 1
i = 1
while True:
    faktorial *= 1
    i += 1
    if i > bilangan:
        break
print(f"Faktorial dari {bilangan} adalah: {faktorial}")

# Melakukan perulangan for untuk jumlah bilangan ganjil
n = 10
total = 0
for i in range(i, n+1):
    if i % 2 != 0:
        total += i
print(f"Jumlah bilangan ganjil dari 1 sampai {n} adalah: {total}")

# Melakukan perulangan while
n = 10
total = 0
i = 1
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1
print(f"Jumlah bilangan ganjil dari 1 sampai {n} adalah: {total}")

# Melakukan perulangan  do-while
n = 10
total = 0
i = 1
while True:
    if i % 2 != 0:
        total += i
    i += 1
    if i >  n:
        break
print(f"Jumlah bilangan ganjil dari 1 sampai {n} adalah: {total}")
