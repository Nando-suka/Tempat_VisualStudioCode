# Menambahkan Library yang dibutuhkan
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk

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
        while j >= 0 and arr [j] > key:
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

# Membuat Prosedur Algoritma Merge sort
def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m + 1, r)
        yield from merge(arr, l, m, r)

# Bagian dari Merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    yield arr

# Menambahkan fungsi yang digunakan untuk melakukan visualisasi dalam algoritma tersebut
def visualize_sorting(arr, algorithm):
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    bars = ax.bar(range(len(arr)), arr, align="edge")

    # Melakukan update dari setiap bar yang digunakan
    def update(arr):
        for bar, val in zip(bars, arr):
            bar.set_height(val)

    anim = animation.FuncAnimation(fig, func=update, frames=algorithm(arr), repeat=False, blit=False)
    plt.show()

# Melakukan random angka 
def generate_random_array(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value, size=(rows, cols)).flatten()

# Memulai visualisasi data
def start_visualization():
    rows = 5
    cols = 4
    min_value = 1
    max_value = 100
    arr = generate_random_array(rows, cols, min_value, max_value)
    
    selected_algorithm = algorithm_var.get()
    if selected_algorithm == "Bubble Sort":
        algorithm = bubble_sort
    elif selected_algorithm == "Insertion Sort":
        algorithm = insertion_sort
    elif selected_algorithm == "Selection Sort":
        algorithm = selection_sort
    elif selected_algorithm == "Quick Sort":
        algorithm = lambda arr: quick_sort(arr, 0, len(arr) - 1)
    elif selected_algorithm == "Merge Sort":
        algorithm = lambda arr: merge_sort(arr, 0, len(arr) - 1)
    else:
        raise ValueError("Unknown algorithm selected")

    visualize_sorting(arr, algorithm)

# GUI setup
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

ttk.Label(root, text="Choose a sorting algorithm:").grid(column=0, row=0, padx=10, pady=10)

algorithm_var = tk.StringVar()
algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Merge Sort"]
algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=algorithms)
algorithm_menu.grid(column=1, row=0, padx=10, pady=10)
algorithm_menu.current(0)  # Default to first algorithm

start_button = ttk.Button(root, text="Start Visualization", command=start_visualization)
start_button.grid(column=0, row=1, columnspan=2, pady=20)

root.mainloop()
