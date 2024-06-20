# Concatenating doubly linked list

class Listnode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addFirst (self, item):
        if len(self) == 0:
            self._head = self._tail = Listnode(item, None, None)
        else:
            newnode = Listnode(item, None, self._head)
            self._head.prev = newnode
            self._head = newnode
        self._length += 1
    
    def addLast (self, item):
        if len(self) == 0:
            self._head = self._tail = Listnode(item, None, None)
        else:
            newnode = Listnode(item, self._tail, None)
            self._tail.link = newnode
            self._tail = newnode
        self._length += 1
    
    def __len__(self):
        return self._length
    
    def _addbetween(self, item, before, after):
        node = Listnode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst (self, item):  
        self._addbetween(item, None, self._head)

    def addlast (self, item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
            before.link = after
        if node is self._tail:
            self._tail = before
    

def __iadd__(self, other):
    if other._head is not None:
        if self._head is None:
            self._head = other._head

        else:
            self._tail.link = other._head
            other._head.prov = self._tail
        self._tail = other._tail
        self._length = self._length + other._length

        # Clean Up the other list
        other.__init__()
    return self

L = DoublyLinkedList()
[L.addlast(i) for i in range(11)]
B = DoublyLinkedList()
[B.addlast(i+11) for i in range(10)]

L += B

n = L._head
while n is not None:
    print(n.data, end=" ")  
    n = n.link