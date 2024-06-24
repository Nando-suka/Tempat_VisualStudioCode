import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight elements being compared
            colors = ['gray'] * len(arr)
            colors[j] = 'red'
            colors[j + 1] = 'red'
            yield arr, colors
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Highlight elements being swapped
                colors = ['gray'] * len(arr)
                colors[j] = 'blue'
                colors[j + 1] = 'blue'
                yield arr, colors
        # Mark the last sorted elements
        colors = ['gray'] * (n - i - 1) + ['green'] * (i + 1)
        yield arr, colors
    # Final state: all elements sorted
    colors = ['green'] * len(arr)
    yield arr, colors

def visualize_sorting(arr, algorithm):
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    bars = ax.bar(range(len(arr)), arr, align="edge")
    
    def update(data):
        arr, colors = data
        ax.clear()
        ax.set_xlim(0, len(arr))
        ax.set_ylim(0, max(arr) + 1)
        bars = ax.bar(range(len(arr)), arr, align="edge", color=colors)
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

    anim = animation.FuncAnimation(fig, func=update, frames=algorithm(arr), repeat=False, blit=False)
    plt.show()

def generate_random_array(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value, size=(rows, cols)).flatten()

def start_visualization():
    rows = 5
    cols = 4
    min_value = 1
    max_value = 100
    arr = generate_random_array(rows, cols, min_value, max_value)
    
    selected_algorithm = algorithm_var.get()
    if selected_algorithm == "Bubble Sort":
        algorithm = bubble_sort
    else:
        raise ValueError("Unknown algorithm selected")

    visualize_sorting(arr, algorithm)

# GUI setup
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

ttk.Label(root, text="Choose a sorting algorithm:").grid(column=0, row=0, padx=10, pady=10)

algorithm_var = tk.StringVar()
algorithms = ["Bubble Sort"]
algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=algorithms)
algorithm_menu.grid(column=1, row=0, padx=10, pady=10)
algorithm_menu.current(0)  # Default to first algorithm

start_button = ttk.Button(root, text="Start Visualization", command=start_visualization)
start_button.grid(column=0, row=1, columnspan=2, pady=20)

root.mainloop()
