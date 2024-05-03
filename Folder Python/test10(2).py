# Belajar menggunakan library part 2
import os 
print(os.getcwd())

# Contoh menggunakan JSON (Javascript Object Notation)
import json
x = '{ "nama": "Fernando", "umur":22, "Kota":"New York"}'

# Parse x

y = json.loads(x)

print(y["umur"])

# Contoh menggunakan Pickle
import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle", "wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

# Kode berikut mengekstraksi berkas dan menaruhnya pada sebuah variable
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary)

# Menggunakan library web scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pengambilan Konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)