contoh = "fernando"

ubah = contoh.replace("fernando", "fernando_tumanggor")
print(ubah)

contoh2 = "  ab c"
contoh3 = "C"
ubah2 = contoh2.lstrip()
ubah4 = contoh2.isspace()
ubah5 = contoh2.isprintable()
ubah6 = contoh2.isascii()
ubah7 = contoh3.isupper()
print(len(contoh2), len(ubah2))
print(ubah2, ubah4, ubah5, ubah6, ubah7)

contoh3 = " or "
contoh4 = " and "
ubah3 = ['fernando', 'okuno', 'chelsea', 'ilmu_komputer']
final = contoh3.join(ubah3)
final2 = contoh4.join(ubah3)
print(final)
print(final2)

# batas
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

# pemanggilan
print(factors(100))

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future

# python input tes
jawaban = input("Siapakah Nama Anda: ")
jawaban2 = input("Tahun Lahir: ")

print()
print("Nama saya adalah", jawaban)
print("Tahun lahir adalah", jawaban2)