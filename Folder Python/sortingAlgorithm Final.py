import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk
import time

# Membuat Prosedur Algoritma bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

# Membuat Prosedur Algoritma Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

# Membuat Prosedur Algoritma Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

# Membuat Prosedur Algoritma Quick sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield arr
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

# Bagian dari Quick sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Membuat Prosedur Algoritma Heap sort
def heap_sort(arr):
    n = len(arr)

    # Membangun heap (reorganisasi array)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)

    # Ekstraksi elemen satu per satu
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # pindah current root ke end
        yield arr
        yield from heapify(arr, i, 0)

# Bagian dari Heap sort
def heapify(arr, n, i):
    largest = i  # Inisialisasi root terbesar sebagai root
    l = 2 * i + 1  # kiri = 2*i + 1
    r = 2 * i + 2  # kanan = 2*i + 2

    # Cek jika anak kiri root ada dan lebih besar dari root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Cek jika anak kanan root ada dan lebih besar dari root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Ganti root jika dibutuhkan
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # tukar
        yield arr
        # Heapify root
        yield from heapify(arr, n, largest)

# Membuat Prosedur Algoritma Shell sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                yield arr
            arr[j] = temp
            yield arr
        gap //= 2

# Menambahkan kode untuk visualisasi
def visualize_sorting(arr, algorithm, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    bars = ax.bar(range(len(arr)), arr, align="edge", color=plt.cm.viridis(np.linspace(0, 1, len(arr))))

    # Tambahkan anotasi angka di atas bar
    annotations = [ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom', color='black', fontsize=10) for bar in bars]

    start_time = time.time()
    
    # Untuk update bar setiap perulangan
    def update(arr):
        current_time = time.time()
        elapsed_time = current_time - start_time

        for bar, val, annotation in zip(bars, arr, annotations):
            bar.set_height(val)
            annotation.set_text(f'{int(val)}')
            annotation.set_y(val)

        ax.set_xlabel(f'Waktu eksekusi: {elapsed_time:.6f} detik')

    anim = animation.FuncAnimation(fig, func=update, frames=algorithm(arr), repeat=False, blit=False)
    plt.show()

# Mengubah input secara random
def generate_random_array(size, min_value, max_value):
    return np.random.randint(min_value, max_value, size=size)

# Memulai visualisasi
def start_visualization():
    size = 30
    min_value = 1
    max_value = 100
    arr = generate_random_array(size, min_value, max_value)
    
    selected_algorithm = algorithm_var.get()
    if selected_algorithm == "Bubble Sort":
        algorithm = bubble_sort
    elif selected_algorithm == "Insertion Sort":
        algorithm = insertion_sort
    elif selected_algorithm == "Selection Sort":
        algorithm = selection_sort
    elif selected_algorithm == "Quick Sort":
        algorithm = lambda arr: quick_sort(arr, 0, len(arr) - 1)
    elif selected_algorithm == "Heap Sort":
        algorithm = heap_sort
    elif selected_algorithm == "Shell Sort":
        algorithm = shell_sort
    else:
        raise ValueError("Unknown algorithm selected")

    visualize_sorting(arr, algorithm, selected_algorithm)

# GUI setup
root = tk.Tk()
root.title("Visualisasi Algoritma Sorting")

ttk.Label(root, text="Memilih Algoritma:").grid(column=0, row=0, padx=10, pady=10)

algorithm_var = tk.StringVar()
algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Heap Sort", "Shell Sort"]
algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=algorithms)
algorithm_menu.grid(column=1, row=0, padx=10, pady=10)
algorithm_menu.current(0)  # Default to first algorithm

start_button = ttk.Button(root, text="Start", command=start_visualization)
start_button.grid(column=0, row=1, columnspan=2, pady=20)

root.mainloop()
