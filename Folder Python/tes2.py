array_angka = [1, 5, 10, 15, 20]
array_angka2 = [2, 4, 9, 14, 19]

# Menggabungkan array menjadi satu
total_array = array_angka + array_angka2
print(total_array)

# Penambahan dalam Array
for i in range(len(array_angka)):
    total = array_angka[i] + array_angka2[i]
    kurang = array_angka[i] - array_angka2[i]
    print(total, end=' ')

# Pengurangan dalam Array
print()
for i in range(len(array_angka)):
    kurang = array_angka[i] - array_angka2[i]
    print(kurang, end=' ')

print()
# Mengurutkan nilai pada array dengan bilangan index yang hanya genap
daftar_array = [2, 1, 3, 9, 10, 11, 5, 4, 3]
daftar_gage = ['ganjil', 'genap', 'ganjil', 'genap', 'ganjil', 'genap', 'ganjil', 'genap', 'ganjil', 'genap']
ukuran = len(daftar_array)
ukuran2 = len(daftar_gage)
daftar_array2 = [0 for i in range(ukuran)]
for i in range(ukuran):
    i *= 2
    if i > ukuran:
        break
    print(daftar_array[i], end=' ')

# batas
print()
daftar_array3 = [10, 20, 30, 40, 50, 60]
ukuran3 = len(daftar_array3)

for i in range(ukuran3):
    if i < 3:
        print(daftar_array3[i], end=' ')

print()
for i in range(ukuran3):
    if i >= 3:
        print(daftar_array3[i], end=' ')

print()

# Pertanyaan sederhana
pernyataan = "Jakarta adalah ibukota Indonesia"
bertanya = input("Apakah nama Ibukota Indonesia?: ")
jawaban = pernyataan.startswith(bertanya)

if jawaban:
    print("Jawaban Anda benar")
else:
    print("Jawaban Anda masih salah")

# Setiap perintah mengandung makna tersendiri
akhiran = "Aku mandi di sungai"
print(akhiran.endswith("sungai"))
print(akhiran.endswith("mandi"))
print(akhiran.isspace())

# Apa lagi yang dibutuhkan untuk menpersonifikassi semua kehidupan yang ada?
# Apakah itu kurang untuk menyatakan suatu perasaaan yang asli?
# Tak peduli semua itu terasa seperti melambung di udara?
# Bahkan betul yang diucpakan oleh Osamu Dazai, dunia ini begitu mengerikan
# Secara intuitif orang yang berkata jujur tidak akan pernah bertahan melawan ancaman yang ada di dunia ini
# Dan selama ini aku selalu salah dalam menempatkan diri untuk mencari kehidupan yang benar
# tidak peduli sesakit apapun itu kehidupan yang ada seharusnya aku berfokus kepada kedua orang tuaku
# merekelah yang memberikan aku kehidupan sehingga aku harus menyadarkan diri dan berbakti kepada kedua orang tua
# hal ini lah yang menjadikan aku tidak sadar dan terkadang lupa atas semua yang telah kuperbuat
# seperti meninggalkan bekas luka yang begitu mendalam dan menyakitkan kepada kedua orang tuaku
# dan juga seharusnya aku melihat seperti afkar, rey, dan yudhistira yang begitu menyayangi kedua orang tua mereka
# harta paling berharha itu yakni adalah keluarga dan orang tua
# jangan pernah engkau melupakan hal tersebut dan terus belajar dari kesalahan yang engkau perbuat
# dan jangan lupa untuk selalu bersyukur
# betapa hebatnya ketika aku menyadari bahwa kedua orang tuaku lah yang bisa membawaku sejauh ini
# aku harus terus mengakui kesalahan yang telah kuperbuat dan terus berbenah demi kedua orang tuaku
# selagi masih hidup di muka bumi ini, seperti perintah hukum taurat ke 5 yang selalu mengatakan
# Hormatilah ayah dan ibumu supaya lanjut umurmu di bumi yang Allah berikan kepada mu.
# INGAT!!! tidak ada yang lebih berharga selain orang tua mu
# oleh karena itu saya selalu bersalah dalam dunia ini
# untuk apa disukai oleh orang  lain, jika orang tua mu saja tidak bisa engkau jaga selalu
# fokuslah kepada orang tuamu selalu
# dan bahagiakan orang tuamu atas prestasi ataupun tujuan nya inigin diraih bersama
# seperti tidak ada ruang
# intinya adalah selalu baik kepada kedua orang tuamu
# jangan nenjadi osamu dazai, tetapi berpikirlah agar dapat merenung yang mendalam sama seperti ia
# Demikian dan Terima Kasih
