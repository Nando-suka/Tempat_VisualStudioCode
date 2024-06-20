class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBeginning (self,newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def printList (self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def deleteFromBeginning (self):
        if self.head is None:
            return "The List is empty"
        self.head = self.head.next

    def deleteFromEnd (self):
        if self.head is None:
            return "The list is empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search (self, value):
        current = self.head 
        position = 0
        while current:
            if current.data == value:
                return f"Value {value} found at position {position}"
            current = current.next
            position += 1
        return f"Value {value} not found in the list"

if __name__ == '__main__':
    list1 = LinkedList()
    list1.InsertAtBeginning('satu')
    list1.InsertAtBeginning('dua')
    list1.InsertAtBeginning('tiga')
    list1.InsertAtBeginning('empat')
    list1.InsertAtBeginning('lima')

    list1.printList()