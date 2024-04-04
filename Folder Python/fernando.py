kontak = {}

def show_menu():
    print('Menu')
    print('1. Tambah Kontak')
    print('2. Edit Kontak')
    print('3. Hapus Kontak')
    print('4.  Keluar')

def add_contact():
    nama = input('Masukkan Nama Kontak : ')
    nomor_handphone = input('Masukkan Nomor telepon : ')
    kontak[nama] = nomor_handphone
    print(f'Kontak {nama} dengan nomor {nomor_handphone} telah diitambahkan.')

def edit_contact():
    edit_nama = input('Masukkan nama kontak yang ingin diedit : ')
    if edit_nama in kontak:
        nama_baru = input('Masukkan nama baru (kosongkan jika ingin mengganti) : ')
        nomor_handphone_baru = input('Masukkan nomor telepon baru (kosongkan jika tidak ingin mengganti)')

        if nama_baru:
            kontak[nama_baru] = kontak.pop(edit_nama)
            print(f'Kontak {edit_nama} berhasil diedit')
        if nomor_handphone_baru:
            kontak[nama_baru] = nomor_handphone_baru
            print(f'Kontak {edit_nama} berhasil diedit')

        print(f'Kontak {edit_nama} tidak diedit')
    else:
        print(f'Kontak {edit_nama} tidak ditemukan')
    
def hapus_kontak():
    hapus_nama = input('Masukkan Nama kontak yang ingin dihapus : ')
    if hapus_nama in kontak:
        del kontak[hapus_nama]
        print(f'Kontak {hapus_kontak} berhasil dihapus')
    else:
        print(f'Kontak {hapus_kontak} tidak ditemukan')

def main():
    while True:
        show_menu()
        pilihan = input('Pilih nomor menu : ')

        if pilihan == '1':
            add_contact()
        elif pilihan == '2':
            edit_contact()
        elif pilihan == '3':
            hapus_kontak()
        elif pilihan == '4':
            print('Terimakasih keluar dari program')
            break
        else:
            print('Pilihan tidak valid. Silahkan pilih nomor pilih menu yang sesuai.')
        
if __name__ == '__main__':
    main()
        

