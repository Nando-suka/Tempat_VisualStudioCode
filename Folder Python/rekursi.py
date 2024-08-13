def reverse(s, start, stop):
    """Reverse element in implicit slice S[start:stop]"""
    if start < stop - 1:                                    # if at least 2 elements
        s[start], s[stop - 1] = s[stop - 1], s[start]       # swap first and last
        reverse(s, start+1, stop-1)                         # recur on test


daftar_angka = [10, 20, 30, 40, 50]
hasil = reverse(daftar_angka, 0, 5)
print(hasil)