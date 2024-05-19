# GCD (Greatest Common Divisor) adalah salah satu jenis algoritma yang memungkinkan untuk mencari
# faktor persekutuan terbesar selain itu jenis dari penyakit 
def gcd (m,n):
    while True:
        r = m % n
        m = n
        n = r
        if (n == 0):
            break
    print(m) 

gcd(60,24)
