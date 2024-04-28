import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from aquarel import load_theme

theme = load_theme("arctic_dark")
theme.apply()

class DataPlotterApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Plotter")
        master.geometry("800x600")  # Mengatur ukuran jendela

        # Daftar data X dan Y untuk setiap grafik
        self.data_entries = []

        # Label sumbu X
        self.xlabel_label = tk.Label(master, text="X Label:")
        self.xlabel_label.pack()
        self.xlabel_entry = tk.Entry(master)
        self.xlabel_entry.pack()

        # Label sumbu Y
        self.ylabel_label = tk.Label(master, text="Y Label:")
        self.ylabel_label.pack()
        self.ylabel_entry = tk.Entry(master)
        self.ylabel_entry.pack()

        # Tombol untuk memilih file Excel
        self.select_file_button = tk.Button(master, text="Select Excel File", command=self.select_excel_file)
        self.select_file_button.pack()

        # Tombol untuk menghapus grafik
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_graph, state=tk.DISABLED)
        self.delete_button.pack()

        # Membuat grafik awal dengan ukuran yang lebih besar
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

    def select_excel_file(self):
        # Memilih file Excel
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            # Memeriksa apakah label sumbu X dan sumbu Y telah dimasukkan
            xlabel = self.xlabel_entry.get()
            ylabel = self.ylabel_entry.get()

            if not xlabel or not ylabel:
                messagebox.showerror("Error", "Please enter both X and Y labels.")
                return

            # Membaca data dari file Excel
            try:
                data = pd.read_excel(file_path)
                x_values = data.iloc[:, 0]  # Mengambil data dari kolom pertama sebagai data X
                y_values = data.iloc[:, 1]  # Mengambil data dari kolom kedua sebagai data Y

                # Menambahkan data X dan Y ke dalam daftar data_entries
                self.data_entries.append((x_values, y_values))

                # Memplot semua data yang sudah dimasukkan
                self.ax.clear()
                for x_data, y_data in self.data_entries:
                    self.ax.plot(x_data, y_data)
                self.ax.set_xlabel(xlabel)  # Menetapkan label sumbu X
                self.ax.set_ylabel(ylabel)  # Menetapkan label sumbu Y
                self.canvas.draw()

                # Mengaktifkan tombol "Delete"
                self.delete_button.config(state=tk.NORMAL)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to read data from Excel file:\n{str(e)}")

    def delete_graph(self):
        # Menghapus grafik
        self.ax.clear()
        self.canvas.draw()

        # Menonaktifkan tombol "Delete"
        self.delete_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = DataPlotterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

theme.apply_transforms()
