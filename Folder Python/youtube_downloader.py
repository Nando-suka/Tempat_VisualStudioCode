import os
from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        # Membuat objek YouTube
        yt = YouTube(url)
        
        # Menampilkan informasi video
        print(f"Judul: {yt.title}")
        print(f"Durasi: {yt.length} detik")
        print(f"Views: {yt.views}")
        print(f"Rating: {yt.rating}")

        # Memilih stream video dengan resolusi tertinggi
        ys = yt.streams.get_highest_resolution()

        # Mengunduh video
        print("Mengunduh...")
        ys.download(output_path)
        print("Download selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ")
    output_path = input("Masukkan folder output (biarkan kosong untuk folder saat ini): ")

    if not output_path:
        output_path = '.'

    # Pastikan folder output ada
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_video(url, output_path)
