import tkinter as tk
from tkinter import messagebox
import json

class AplikasiKaryawan:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Data Karyawan")

        self.frame_data = tk.Frame(root)
        self.frame_data.pack(pady=10)

        # Label dan Entry untuk Nama
        self.label_nama = tk.Label(self.frame_data, text="Nama:")
        self.label_nama.grid(row=0, column=0, sticky="w")
        self.entry_nama = tk.Entry(self.frame_data)
        self.entry_nama.grid(row=0, column=1)

        # Label dan Entry untuk Usia
        self.label_usia = tk.Label(self.frame_data, text="Usia:")
        self.label_usia.grid(row=1, column=0, sticky="w")
        self.entry_usia = tk.Entry(self.frame_data)
        self.entry_usia.grid(row=1, column=1)

        # Tombol Tambah Karyawan
        self.btn_tambah = tk.Button(root, text="Tambah Karyawan", command=self.tambah_karyawan)
        self.btn_tambah.pack(pady=5)

        # Label dan Entry untuk Pencarian
        self.label_search = tk.Label(root, text="Cari Nama:")
        self.label_search.pack()
        self.entry_search = tk.Entry(root)
        self.entry_search.pack()

        # Tombol Cari
        self.btn_cari = tk.Button(root, text="Cari", command=self.cari_karyawan)
        self.btn_cari.pack()

        # Listbox untuk menampilkan data karyawan
        self.listbox_karyawan = tk.Listbox(root, width=50)
        self.listbox_karyawan.pack()

        # Tombol Edit Karyawan
        self.btn_edit = tk.Button(root, text="Edit Karyawan", command=self.edit_karyawan)
        self.btn_edit.pack()

        # Tombol Hapus Karyawan
        self.btn_hapus = tk.Button(root, text="Hapus Karyawan", command=self.hapus_karyawan)
        self.btn_hapus.pack()

        # Tombol Simpan Data
        self.btn_simpan = tk.Button(root, text="Simpan Data", command=self.simpan_data)
        self.btn_simpan.pack()

        # Tombol Muat Data
        self.btn_muat = tk.Button(root, text="Muat Data", command=self.muat_data)
        self.btn_muat.pack()

    def tambah_karyawan(self):
        nama = self.entry_nama.get()
        usia = self.entry_usia.get()

        if nama and usia:
            self.listbox_karyawan.insert(tk.END, f"Nama: {nama}, Usia: {usia}")
            self.entry_nama.delete(0, tk.END)
            self.entry_usia.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Silakan masukkan nama dan usia karyawan!")

    def cari_karyawan(self):
        nama_cari = self.entry_search.get()
        if not nama_cari:
            messagebox.showwarning("Peringatan", "Silakan masukkan nama untuk pencarian!")
            return
        
        ditemukan = False
        for i in range(self.listbox_karyawan.size()):
            data_karyawan = self.listbox_karyawan.get(i)
            if f"Nama: {nama_cari}" in data_karyawan:
                self.listbox_karyawan.selection_clear(0, tk.END)
                self.listbox_karyawan.selection_set(i)
                self.listbox_karyawan.see(i)
                ditemukan = True
                break
        
        if not ditemukan:
            messagebox.showinfo("Info", f"Tidak ditemukan karyawan dengan nama '{nama_cari}'.")

    def edit_karyawan(self):
        indeks_terpilih = self.listbox_karyawan.curselection()
        if not indeks_terpilih:
            messagebox.showwarning("Peringatan", "Silakan pilih karyawan yang ingin di edit.")
            return
        
        indeks = indeks_terpilih[0]
        data_karyawan = self.listbox_karyawan.get(indeks)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        nama_awal, usia_awal = self.extract_data_karyawan(data_karyawan)
        
        # Munculkan dialog edit
        dialog_edit = tk.Toplevel(self.root)
        dialog_edit.title("Edit Karyawan")
        
        label_nama = tk.Label(dialog_edit, text="Nama:")
        label_nama.grid(row=0, column=0)
        entry_nama = tk.Entry(dialog_edit)
        entry_nama.insert(0, nama_awal)
        entry_nama.grid(row=0, column=1)
        
        label_usia = tk.Label(dialog_edit, text="Usia:")
        label_usia.grid(row=1, column=0)
        entry_usia = tk.Entry(dialog_edit)
        entry_usia.insert(0, usia_awal)
        entry_usia.grid(row=1, column=1)

        # Tombol simpan edit
        btn_simpan = tk.Button(dialog_edit, text="Simpan", command=lambda: self.simpan_edit(dialog_edit, indeks, entry_nama.get(), entry_usia.get()))
        btn_simpan.grid(row=2, columnspan=2)

    def simpan_edit(self, dialog_edit, indeks, nama_baru, usia_baru):
        if nama_baru and usia_baru:
            self.listbox_karyawan.delete(indeks)
            self.listbox_karyawan.insert(indeks, f"Nama: {nama_baru}, Usia: {usia_baru}")
            dialog_edit.destroy()
        else:
            messagebox.showwarning("Peringatan", "Silakan masukkan nama dan usia karyawan!")

    def hapus_karyawan(self):
        indeks_terpilih = self.listbox_karyawan.curselection()
        if not indeks_terpilih:
            messagebox.showwarning("Peringatan", "Silakan pilih karyawan yang ingin dihapus.")
            return
        
        indeks = indeks_terpilih[0]
        self.listbox_karyawan.delete(indeks)

    def simpan_data(self):
        data_karyawan = [self.listbox_karyawan.get(i) for i in range(self.listbox_karyawan.size())]
        with open("data_karyawan.json", "w") as file:
            json.dump(data_karyawan, file)
        messagebox.showinfo("Info", "Data karyawan berhasil disimpan!")

    def muat_data(self):
        try:
            with open("data_karyawan.json", "r") as file:
                data_karyawan = json.load(file)
            self.listbox_karyawan.delete(0, tk.END)
            for data in data_karyawan:
                self.listbox_karyawan.insert(tk.END, data)
            messagebox.showinfo("Info", "Data karyawan berhasil dimuat!")
        except FileNotFoundError:
            messagebox.showwarning("Peringatan", "File data karyawan tidak ditemukan!")

    def extract_data_karyawan(self, data_karyawan):
        data = data_karyawan.split(", ")
        nama = data[0].split(": ")[1]
        usia = data[1].split(": ")[1]
        return nama, usia

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiKaryawan(root)
    root.mainloop()