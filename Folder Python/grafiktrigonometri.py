import numpy as np
import matplotlib.pyplot as plt
from math import *
import sympy as sp

def plot_trigonometry(expr, x_range=(-2*np.pi, 2*np.pi), num_points=1000):
    """
    Plots a trigonometric function based on the expression given.

    Parameters:
        expr (str): The trigonometric expression to plot, e.g., 'sin(x)'
        x_range (tuple): The range of x values over which to plot
        num_points (int): The number of points to calculate

    Returns:
        None
    """
    # Mengubah string input ke dalam fungsi yang dapat di-evaluasi
    x = sp.symbols('x')
    try:
        func = sp.lambdify(x, sp.sympify(expr), 'numpy')
    except (SyntaxError, ValueError) as e:
        print(f"Error: {e}")
        return

    # Membuat data untuk x dan y
    x_vals = np.linspace(x_range[0], x_range[1], num=num_points)
    y_vals = func(x_vals)

    # Membuat grafik
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label=f'y = {expr}')
    plt.title('Grafik Fungsi Trigonometri')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.show()

# Mengambil input dari pengguna
expression = input("Masukkan rumus trigonometri (gunakan 'x' sebagai variabel): ")
plot_trigonometry(expression)
