def binary_sum(data, start, stop):
    """Return the sum of the numbers in implicit slice s[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return data[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(data, start, mid) + binary_sum(data, mid, stop)

daftar = [10, 92, 39, 4, 2, 49, 42, 12]
hasil = binary_sum(daftar, 0, 6)
print(hasil)
