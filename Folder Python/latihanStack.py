# Pertama mengusahakan agar mengerti prinsip dari stack, yakni last in first out

# Membuat program stack
""" def create_push_list ():
    stack = []
    return stack

def check (stack):
    return len (stack) == 0

def push (stack,item):
    stack.append(item)
    print("Telah ditambahkan: ", item)


def pop (stack):
    if (check(stack)):
        return "Stak Anda kosong"
    
    return stack.pop()

stack = create_push_list()
push(stack,2)
push(stack,4)
push(stack,8)
print("Berikut yang ditampilkan: ", pop(stack))
 """

# Membuat program stack karakter huruf dibalik
def create ():
    stack = []
    return stack

def check (stack):
    return len(stack) == 0

def push (stack,item):
    stack.append(item)
    print(item, end="")

def pop (stack):
    if (check(stack)):
        return "Input tidak ada (kosong)"
    else:
       return stack.pop()
                  

karakter = create()
push(karakter,"A")
push(karakter,"k")
push(karakter,"u")
print()
print("Tampilan yang ditampilkan: ", pop(karakter),pop(karakter),pop(karakter))

# Perbaikan dari Chatgpt
def create ():
    return []

def is_empty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)

def pop (stack):
    if (is_empty(stack)):
        return "Stack Kosong"
    else:
        return stack.pop()
    
def reverse_string (input_string):
    stack = create()
    for char in input_string:
        push(stack,char)

    reversed_string =  ''

    while not is_empty(stack):
        reversed_string += pop(stack)

    return reversed_string

# Contoh penggunaan
input_string = "Aku"
print("String yang asli: " + input_string)
reversedd_string = reverse_string(input_string)
print("String yang dibalikkan: " + reversedd_string)