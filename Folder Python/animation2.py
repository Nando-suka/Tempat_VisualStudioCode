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

# Membuat array acak
def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


# Contoh penggunaan dengan array acak
arr = generate_random_array(10, 1, 100)
bubble_sort_visualize(arr)
