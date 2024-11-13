import numpy as np

# Membuat dua matriks 4x4
matriks_1 = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

matriks_2 = np.array([[16, 15, 14, 13],
                      [12, 11, 10, 9],
                      [8, 7, 6, 5],
                      [4, 3, 2, 1]])

# Penjumlahan Matriks
penjumlahan = matriks_1 + matriks_2

# Pengurangan Matriks
pengurangan = matriks_1 - matriks_2

# Perkalian Matriks
perkalian = np.dot(matriks_1, matriks_2)

# Determinan Matriks
determinan_1 = np.linalg.det(matriks_1)
determinan_2 = np.linalg.det(matriks_2)

# Matriks Invers (jika ada)
try:
    invers_1 = np.linalg.inv(matriks_1)
    invers_2 = np.linalg.inv(matriks_2)
except np.linalg.LinAlgError:
    invers_1 = invers_2 = None

# Menampilkan hasil
print("Matriks 1:")
print(matriks_1)

print("\nMatriks 2:")
print(matriks_2)

print("\nPenjumlahan Matriks 1 dan Matriks 2:")
print(penjumlahan)

print("\nPengurangan Matriks 1 dan Matriks 2:")
print(pengurangan)

print("\nPerkalian Matriks 1 dan Matriks 2:")
print(perkalian)

print(f"\nDeterminan Matriks 1: {determinan_1}")
print(f"Determinan Matriks 2: {determinan_2}")

if invers_1 is not None:
    print("\nInvers Matriks 1:")
    print(invers_1)
else:
    print("\nMatriks 1 tidak memiliki invers.")

if invers_2 is not None:
    print("\nInvers Matriks 2:")
    print(invers_2)
else:
    print("\nMatriks 2 tidak memiliki invers.")
