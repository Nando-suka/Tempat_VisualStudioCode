import json
import time

class LCG:
    def __init__(self) -> None:
        self.m = 281474976710656
        self.a = 25214903917
        self.c = 11
        self.seed = round(time.time_ns())

    def next (self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return (self.seed - (self.seed & 32767)) >> 16

def main() -> None:
    # Base 62 characters
    alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Menginisialisasi LCG
    lcg = LCG()

    # Membuka data json ke directory
    with open("data.json", "r") as f:
        data = json.load(f)

    if __name__ == '__main__':
        while True:
            link_input = input("Masukkan link yang ingin dipendekkan: ")
            print()

            done = False

            while not done:
                print(
                    "Masukkan nama link (jika kosong akan diisi dengan alphanmueric random"
                )
                output = input("shorten.er/")

                if output == "":
                    rand_val = ""
                    for i in range(8):
                        rand_val += alphanumeric[lcg.next() % 62]
                    link_output = "shorten.er/" + rand_val

                    while link_output in data.keys():
                        rand_val = ""
                        for i in range(8):
                            rand_val += alphanumeric[lcg.next() % 62]
                        link_output = "shorten.er/" + rand_val

                    print(f"Link berhasil disingkat: {link_output}")

                    data[link_output] = link_input
                    done = True

                else:
                    link_output = "shorten.er/" + output
                    if link_output in data.keys():
                        print("Nama Link sudah ada di database")
                    else:
                        data[link_output] = link_input
                        done = True
                        lanjut = input("Masih ingin lanjut? [Y/n]: ")
                        print()
                        if lanjut.lower() == "n":
                            break

        print("Terima kasih sudah menggunakan program kami")
        with open("data.json", "w") as f:
            json.dump(data, f)

# Seketika mengingat hal ini dapat menjadi ambiguitas
# Penggunaan LCG untuk membangkitkan bilangan acak secara semu dengan efisien dan efek
# Linear Congruential Generator

