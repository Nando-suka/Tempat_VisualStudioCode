import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

def insertion_sort_visualize(arr):
    # Mengubah array multi dimensi menjadi satu dimensi
    flat_arr = arr.flatten()
    
    # Membuat figure dan axes untuk plotting
    fig, ax = plt.subplots()
    
    # Mengatur batasan x dan y
    ax.set_xlim(0, len(flat_arr))
    ax.set_ylim(0, max(flat_arr) + 1)
    
    # Bar yang akan kita animasikan
    bars = ax.bar(range(len(flat_arr)), flat_arr, align="edge")
    
    # Label sumbu x
    ax.set_xticks(range(len(flat_arr)))
    
    # Fungsi untuk update bar di setiap frame
    def update(frame):
        ax.clear()
        ax.set_xlim(0, len(flat_arr))
        ax.set_ylim(0, max(flat_arr) + 1)
        ax.set_xticks(range(len(flat_arr)))
        for i in range(1, frame + 1):
            key = flat_arr[i]
            j = i - 1
            while j >= 0 and key < flat_arr[j]:
                flat_arr[j + 1] = flat_arr[j]
                j -= 1
            flat_arr[j + 1] = key
        bars = ax.bar(range(len(flat_arr)), flat_arr, align="edge")
        return bars
    
    # Membuat animasi
    anim = animation.FuncAnimation(fig, update, frames=range(len(flat_arr)), repeat=False)
    
    # Menampilkan animasi
    plt.show()

# Membuat array multi dimensi acak
def generate_random_multi_dim_array(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value, size=(rows, cols))

# Contoh penggunaan dengan array multi dimensi acak
arr = generate_random_multi_dim_array(10, 4, 1, 100)
print("Array sebelum diurutkan:")
print(arr)
insertion_sort_visualize(arr)
print("Array setelah diurutkan:")
print(arr.reshape(5, 4))
