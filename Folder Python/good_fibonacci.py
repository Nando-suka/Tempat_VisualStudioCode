def good_fibonacci(n):
    """Return pair of fibonacci numbers F(n) and F(n-1)"""
    if n < 1:
        return(n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return(a+b, a)

def linier_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linier_sum(S, n-1) + S[n - 1]

daftar_angka = [10, 20, 30, 40, 50]
print((linier_sum(daftar_angka, 5)))

# recursive algorithms for computing powers
