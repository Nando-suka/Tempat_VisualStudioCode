def is_balanced (expression):
    # Maping dari simbol penutup ke simbol terbuka
    matching_bracket = {')':'(','}':'{',']':'['}
    stack = []

    for char in expression:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack.pop() != matching_bracket[char]:
                return False    
            
    return not stack

# Menerima input langsung dari user
user_input = input("Masukkan sebuah ekspresi untuk diperiksa apakah seimbang:")
print("Balanced" if is_balanced(user_input) else "Not Balanced")