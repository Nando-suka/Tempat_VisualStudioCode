# Belajar Linked List Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def hapusvalue(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def printlist(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print('None')


# Contoh penggunaan
my_list = Linkedlist()   # Konstruktor

# Menambahkan elemen
my_list.append(1)
my_list.append(10)
my_list.append(100)
my_list.append(1000)

# Menampilkan list
my_list.printlist()

# Menyisipkan elemen di awal
my_list.prepend(0)
my_list.printlist()

# Menambahkan elemen kedua kalinya
my_list.append(10000)
try:
    my_list.append()
except TypeError:
    print("Error: masukkan argumen nya bro . . .")
my_list.printlist()

# Menghapus elemen
my_list.hapusvalue(10)
my_list.printlist()

print()
print('----- Untuk Array ------')
# Penghapusan array
angkalist = [10, 20, 30, 40, 50]

angkalist.remove(20)
print(angkalist)
