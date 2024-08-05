class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singlylinkedlist:
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

    def printlist(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print(None)


inputan = Singlylinkedlist()  # Konstruktor

inputan.append(10)
inputan.append(15)
inputan.append(20)
inputan.append(25)
inputan.append(30)
inputan.printlist()

bertanya = int(input("Masukkan angka: "))

inputan.append(bertanya)
inputan.printlist()
print(type(inputan))

# Terlalu tersering dan tersulit untuk selalu dapat menampilkan kode dan kesukaan nya
