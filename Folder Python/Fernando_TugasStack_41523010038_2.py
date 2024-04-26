# Implementasi stack dengan list Python
""" def create_stack ():
    stack = []
    return stack

def check_empty (stack):
    return len(stack) == 0

def push (stack, item):
    stack.append(item)
    print("Pushed item: " + item)

def pop (stack):
    if (check_empty(stack)):
        return "stack is empty"
    
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("Popped item: " + pop(stack))
print("Stack after popping an element: " + str(stack)) """

def membuat_tumpukan ():
    stack = []
    return stack

def mengecek_kosong (stack):
    return len(stack) == 0

def dorongan (stack, item):
    stack.append(item)
    print("Barang ditambahkan: " + item)

def pop (stack):
    if (mengecek_kosong(stack)):
        return "Tumpukan kosong"
    
    return stack.pop()

stack = membuat_tumpukan()
dorongan(stack, "Fernando")
dorongan(stack, "Tumanggor")
dorongan(stack, "Chelsea")
dorongan(stack, "Haikyuu")

print("Menjadikan ini menjadi list: " + str(stack))