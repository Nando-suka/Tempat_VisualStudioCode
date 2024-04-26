""" from collections import deque

def create_stack ():
    stack = deque
    return stack

def push (stack, item):
    stack.append(item)

def pop (stack):
    if(stack):
        print("Elemen popped from stack")
        print(stack.pop)
    else:
        print("Stack is empty")

def show (stack):
    print("Stack elements are ")
    print(stack)

new_stack = create_stack()
push(new_stack,25)
push(new_stack,56)
push(new_stack,32)
show(new_stack) """
""" 
from queue import LifoQueue

def new ():
    stack = LifoQueue(maxsize=3)
    return stack

def push (stack,item):
    if(stack.full):
        print("The stack is already full")
    else:
        stack.pull(item)
        print("Size:",stack.qsize)

def pop (stack):
    if(stack.empty):
        print("Stack is empty")
    else:
        print("Element popped from the stack is", stack.get)
        print("Size:", stack.qsize)

stack = new()
pop(stack)
push(stack,32)
push(stack,56)
push(stack,67)
pop(stack)
 """

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__ (self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        val = self.head.next
        show = ""
        while val:
            show += str(val.value) + "."
            val = val.next
        return show[:-3]
    
    def get_size (self):
        return self.size
    
    def isEmpty (self):
        return self.size == 0
    
    def peek (self):
        if self.isEmpty():
            raise Exception("This is an empty stack")
        return self.head.next
        
    def push (self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = None
        self.size += 1

    def pop (self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        remove = self.head.next
        self.head.next = self.head.next
        self.size -= 1
        return remove
    
if __name__ == "__main__":
    stack = Stack()
    n = 20  
    for i in range(1, 11):
        stack.push(n)
        n += 5
    print(f"Stack:{stack}")

    for i in range (1,6):
        remove = stack.pop()
        print(f"Pop {remove}")
    print(f"Stack: {stack}")