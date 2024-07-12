import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    line, = ax.plot(range(len(arr)), arr, marker='o')
    ax.set_xlim(0, n - 1)
    ax.set_ylim(0, max(arr) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_line(array, line, iteration):
        line.set_ydata(array)
        iteration[0] += 1
        text.set_text(f"Iteration: {iteration[0]}")

    def animate(i):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                update_line(arr, line, iteration)
        return line

    anim = animation.FuncAnimation(fig, animate, frames=n, interval=500, repeat=False)
    plt.show()

def generate_random_array(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value, size=(rows, cols)).flatten()


# Meminta input dari pengguna
print("==== Menu ====")
print("1. Random\n2. Pengguna")
pilihan = int(input("Silahkan masukkan pilihan (1/2): "))

if pilihan == 1:
    rows = 5
    cols = 4
    min_value = 1
    max_value = 100
    arr = generate_random_array(rows, cols, min_value, max_value)
    bubble_sort(arr)
elif pilihan == 2:
    input_data = input("Masukkan angka-angka yang ingin diurutkan, pisahkan dengan koma: ")
    data = list(map(int, input_data.split(',')))
    bubble_sort(data)
else:
    print("Pilihan tidak terdaftar")
