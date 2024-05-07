penanda = {
  "Kota": "Jakarta Barat",
  "provinsi": "Jakarta",
}
print(penanda)

penanda ["Kota"] = "Jakarta Timur"
print(penanda["Kota"])
print(penanda)

# Membuat ternary operator
bertanya = input("Apakah nama dari ibukota Filipina?: ")

jawaban = "Iya benar" if bertanya == "Manila" else "Jawaban Anda masih belum benar"
print(jawaban)

data = {}

for key, value in zip(["nama", "umur", "pekerjaan"], ["Budi", 27, "Guru"]):
  data[key] = value

# Menambahkan nilai baru
data["alamat"] = "Jalan Anyelir No. 1"
data["hobi"] = ["membaca", "menulis", "bermain musik"]

#print(data)

pemain = {}
for kay2, value2 in zip([1,2,3],["Arsenal","Manchester City","Liverpool"]):
  pemain[kay2] = value2

print(pemain)
print(pemain[2])
print(pemain[3])

# Melihat semua nilai
nilai = pemain.values()
print(nilai)

# membuat daftar pemain chelsea berdasarkan posisi
chelsea = {
  "Bek": ["Chalobah","Silva","Disasi","Badiashille"],
  "Gelandang": ["Caicedo","Gallagher","Enzo","Cesadai"],
  "Penyerang": ["Jackson","Mudryk","Palmer"]
}

print(chelsea)
print(chelsea["Bek"][1])

daftar = {
  "Nama": [],
  "Alamat": [],
}


yut = []
yut.append(10)
yut.append(10)
yut.append(20)
print(yut)

while True:
  pertanyaan = input("Masukkan Nama: ")
  pertanyaan2 = input("Masukkan Alamat: ")

  print("Data disimpan.")
  pertanyaan3 = input("Apakah Anda masih ingin melanjutkan? [y/t]:")
  if pertanyaan3 == "y" or pertanyaan3 == "Y":
    pass
  elif pertanyaan3 == "t" or pertanyaan3 == "T":
    break
  else:
    print("Tidak ditemukan silahkan masukkan kembali")
    pertanyaan3 = input("Apakah Anda masih ingin melanjutkan? [y/t]:")