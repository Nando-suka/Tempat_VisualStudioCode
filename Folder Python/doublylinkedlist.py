class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doublylinkedlist:
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
            new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print("None")


if __name__ == "__main__":
    asup = Doublylinkedlist()

    asup.append(5)
    asup.append(10)
    asup.append(15)
    asup.append(20)
    asup.append(25)
    asup.append(30)
    asup.print_list()
