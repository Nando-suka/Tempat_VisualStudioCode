class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} telah masuk ke dalam antrian.")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Antrian kosong. Tidak ada item untuk dihapus.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Antrian kosong.")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Isi antrian: ", end="")
            print(" <- ".join(self.items))
        else:
            print("Antrian kosong.")

# Contoh penggunaan
antrian = Queue()
antrian.enqueue("Mahasiswa 1")
antrian.enqueue("Mahasiswa 2")
antrian.enqueue("Mahasiswa 3")

antrian.display()

print(f"Yang pertama dalam antrian: {antrian.peek()}")

print(f"{antrian.dequeue()} telah keluar dari antrian.")
antrian.display()

print(f"Jumlah item dalam antrian: {antrian.size()}")
