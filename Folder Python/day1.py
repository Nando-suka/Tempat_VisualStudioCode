import tkinter as tk
window = tk.Tk()
# Menambahkan label pertama
tk.Label(text="Label1").pack()
window.update()
teksSaya = input("Masukkan teks yang Anda inginkan: ")
tk.Label(text=teksSaya).pack()
window.update()


# Lindungi batasan waktu