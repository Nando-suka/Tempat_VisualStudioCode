import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort_visualize(arr):
    # Membuat figure dan axes untuk plotting
    fig, ax = plt.subplots()
    
    # Mengatur batasan x dan y
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    
    # Bar yang akan kita animasikan
    bars = ax.bar(range(len(arr)), arr, align="edge")
    
    # Label sumbu x
    ax.set_xticks(range(len(arr)))
    
    # Fungsi untuk update bar di setiap frame
    def update(frame):
        ax.clear()
        ax.set_xlim(0, len(arr))
        ax.set_ylim(0, max(arr) + 1)
        ax.set_xticks(range(len(arr)))
        for i in range(len(arr) - frame - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        bars = ax.bar(range(len(arr)), arr, align="edge")
        return bars
    
    # Membuat animasi
    anim = animation.FuncAnimation(fig, update, frames=range(len(arr)), repeat=False)
    
    # Menampilkan animasi
    plt.show()

# Contoh penggunaan
tanya = int(input("Masukkan Angka: "))
while tanya != 0:
    list_angka = []
    list_angka.append(tanya)
    tanya = int(input("Masukkan Angka: "))

bubble_sort_visualize(list_angka)
