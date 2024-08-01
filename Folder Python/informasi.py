print("\t\tSelamat Datang")
print("Pilihan Informasi")
print("1. Tambah Kontak\n2. Lihat Kontak\n3. Hapus Kontak\n4. Keluar")

pertanyaan = int(input("Silahkan masukkan pilihan Anda: "))
kontak = []
while pertanyaan < 4:
    def tambah(n):
        kontak.append(n)

    def lihatkontak(n, key):
        for i in range(0, len(n)):
            if key == n[i]:
                return key
        return - 1

    def hapuskontak(n, key):
        for i in range(0, len(n)):
            if key == n[i]:
                n.remove(key)
                return
        return - 1

    def isempty():
        if len(kontak) == 0:
            return 0

    # Output
    if pertanyaan == 1:
        nama = input("Masukkan Nama: ")
        tambah(nama)
        print("Input telah ditambahkan")
        bertanyaKembali = input("Apakah Anda ingin memasukkan data kembali? [y/t]: ")
        while bertanyaKembali == 'y':
            nama = input("Masukkan Nama: ")
            tambah(nama)
            print("Input telah ditambahkan")
            bertanyaKembali = input("Apakah Anda ingin memasukkan data kembali? [y/t]: ")
        print(kontak)
    elif pertanyaan == 2:
        mencari = input("Masukkan Nama yang Anda ingin cari: ")
        jawaban = lihatkontak(kontak, mencari)
        if jawaban == -1:
            print("Maaf Nama yang Anda cari tidak ditemukan")
        else:
            print("Kontak Anda ditemukan")
    elif pertanyaan == 3:
        bertanyaKembali = input("Apakah Anda ingin menghapus data? [y/t]: ")
        while bertanyaKembali == 'y':
            mencari2 = input("Masukkan nama yang Anda ingin hapus: ")
            jawaban2 = hapuskontak(kontak, mencari2)
            if jawaban2 == -1:
                print("Maaf Nama tidak ditemukan")
            else:
                print("Kontak telah dihapus")
            bertanyaKembali = input("Apakah Anda ingin menghapus data kembali? [y/t]: ")
    else:
        print("Anda keluar")

    print("\t\tSelamat Datang")
    print("Pilihan Informasi")
    print("1. Tambah Kontak\n2. Lihat Kontak\n3. Hapus Kontak\n4. Keluar")

    pertanyaan = int(input("Silahkan masukkan pilihan Anda: "))
#
