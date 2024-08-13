class Data:
    def __init__(self, nama, nim, jurusan, tahunlahir):
        self._nama = nama
        self._nim = nim
        self._jurusan = jurusan
        self._tahunlahir = tahunlahir

    def getNama(self):
        """Mengembalikan nama mahasiswa"""
        return self._nama

    def getNim(self):
        """Mengembalikan nomor induk mahasiswa"""
        return self._nim

    def get_jurusan(self):
        """Menngembalikan jurusan yang diambil oleh mahasiswa"""
        return self._jurusan

    def getTahunlahir(self):
        """Mengembalikan tahun lahir mahasiswa"""
        return self._tahunlahir

if __name__ == '__main__':

    data = [
        Data("Fernando", 41523010038, 'Teknik Informatika', 2005),
        Data("Maholi", 461253609031, 'Cyber Security', 2007),
        Data("Sutrisno", 810246168088, 'Teknik Mesin', 2006),
        Data("Asep", 12314566622, 'Public Relation', 2005),
    ]
    jumlahdata = len(data)

    for informasi in range(jumlahdata):
        print("Nama: ", data[informasi].getNama())
        print("NIM: ", data[informasi].getNim())
        print("Jurusan:", data[informasi].get_jurusan())
        print("Tahun Lahir:", data[informasi].getTahunlahir())
        print()