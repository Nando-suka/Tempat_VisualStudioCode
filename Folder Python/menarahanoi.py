""" def solusi (n,a,t,r):
    if (n == 0):
        return
    else:
        solusi (n-1,a,t,r)
        print(f"Memindahkan cakram dari {a}, ke {t}")
 """
""" def solve_hanoi(n, source, auxiliary, target):
    if n == 0:
        return
    else:
        # Move n-1 disks from source to auxiliary, so they are out of the way
        solve_hanoi(n-1, source, target, auxiliary)
        
        # Move the nth disk from source to target
        print(f"Pindahkan Cakram dari {source} ke {target}")
        
        # Move the n-1 disks from auxiliary to target
        solve_hanoi(n-1, auxiliary, source, target)

# Example usage
n = 64  # Number of disks """
#solve_hanoi(n, 'A', 'B', 'C') 

def count_hanoi_moves(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * count_hanoi_moves(n - 1)

# Menghitung jumlah gerakan untuk n = 64
print(count_hanoi_moves(64))  # Ini akan mengembalikan 2^64 - 1