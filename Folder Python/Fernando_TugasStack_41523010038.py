class Stack:
    def __init__ (self):
        self.items = []

    def push (self, item):
        self.items.append(item)
    
    def pop (self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty (self):
        return len (self.items) == 0
    
    def peek (self):
        if not self.is_empty():
            return self.items[-1]

    def size (self):
        return len(self.items)    

# Contoh penggunaan stack
stack = Stack()
stack.push(0)
stack.push(9)
stack.push(2)
print(stack.pop())
print(stack.peek())
print(stack.size())


bl = (([(10,10,20),(40,20,10),(5,6,7)]))
print(bl)
print(bl[0])
print(bl[0][2])
bl.append([5,5,5])
print(bl)
