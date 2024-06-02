from collections import deque
from time import perf_counter

_listlagu = ['lagu_satu','lagu_dua','lagu_tiga']
_tuplelagu = ('lagu_satu','lagu_dua','lagu_tiga')
_setlagu = {'lagu_satu','lagu_dua','lagu_tiga'}
_dictlagu = {'1': 'lagu_satu', '2': 'lag_dua', '3': 'lagu_tiga'}

deque_from_list = deque(_listlagu)
deque_from_tuple = deque(_tuplelagu)
deque_from_setlagu = deque(_setlagu)
deque_from_key = deque(_dictlagu.keys())
deque_from_value = deque(_dictlagu.values())

print(deque_from_list)
print(deque_from_value)
print(deque_from_tuple)
print(deque_from_setlagu)
print(deque_from_key)

print()

# Struktur data menggunaka deque
laptop = deque(['Acer', 'Asus', 'Axioo', 'HP', 'Lenovo'])
laptop.appendleft('Dell')
print(laptop)
laptop.popleft()
print(laptop)
laptop.remove('Asus')
print(laptop)
laptop.extendleft(['Toshiba', 'Apple'])
print(laptop)
laptop.rotate()
print(laptop)
laptop.reverse()
print(laptop)
print('Panjang laptop adalah:', len(laptop))
print(sorted(laptop))
print(max(laptop))
print(min(laptop))

# Implementasi 
list_queues = []
list_stack = []

for i in range (3):
    list_queues.insert(0,i)
    list_stack.append(i)

for i in range (3):
    print("Queue: ", list_queues.pop())
    print("Stack: ", list_stack.pop())

queue = deque()
stack = deque()

for i in range(3):
    queue.append(i)
    stack.append(i)

for i in range(3):
    print("Queue: ", queue.popleft())
    print("Stack: ", stack.pop())

t1 = perf_counter()

n = 400_000
for i in range(n):
    queue.append(i)

for i in range(n):
    queue.popleft()

t_queue = perf_counter() - t1
print("deque: ", perf_counter()-t1)

t1 = perf_counter()
#for i in range(n):
#    list_queues.insert(0,i)

#for i in range(n):
#    list_queues.pop()

t_list = perf_counter() - t1
print("List: ", t_list)
print(f"deque is {t_list/t_queue:.2f} times faster")

t1 = perf_counter()

for i in range(n):
    queue.append(i)

for i in range(n):
    queue.pop()

t_queue = perf_counter() - t1
print("stack with deque: ", perf_counter() - t1)

t1 = perf_counter()
for i in range(n):
    list_queues.append(i)

#for i in range(n):
#    list_queues.pop(0)

t_list = perf_counter() -t1
print("list:", perf_counter() - t1)
print(f"stack with deque is {t_list/t_queue:.2f} times faster")