class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Contoh penggunaan stack untuk konversi infix ke postfix
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []

    for char in expression:
        if char.isalnum():  # Operand (alphanumeric characters)
            output.append(char)
        elif char == '(':  # Left parenthesis
            stack.push(char)
        elif char == ')':  # Right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the left parenthesis
        else:  # Operator
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence[char] <= precedence[stack.peek()]):
                output.append(stack.pop())
            stack.push(char)

    # Pop all the operators from the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

# Contoh penggunaan
expression = "a+b*(c^d-e)^(f+g*h)-i"
postfix = infix_to_postfix(expression)
print(f"Infix: {expression}")
print(f"Postfix: {postfix}")
