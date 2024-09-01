# Belajar dalam membuat Breadth First Search Algorithm


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

graph2 = {
    'a': ['e', 'g', 'b'],
    'b': [],
    'c': ['d'],
    'd': [],
    'e': ['f', 'c'],
    'f': [],
    'g': []
}
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=' ')

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


if __name__ == '__main__':
    print("Berikut adalah tampilan dari Breadth First Search ")
    bfs(visited, graph, '5')
    print()
    bfs(visited, graph2, 'a')

# Seperti biasa bahwa breadth first search algorith merupakan algoritma yang mengunjungi terlebih dahulu sekitarnya
# Sedangkan algortima depth first search algotihm merupakan algoritma yang mengunjungi setiap kedalaman dari graphnya


graph3 = {
    '1': ['2', '4'],
    '2': ['3','5'],
    '3': [],
    '4': ['6'],
    '5': ['6'],
    '6': []
}

print()
# Batas yang ada
kosong = []
kosong2 = []
kosong.append('1')
kosong2.append('1')

while kosong2:
    m = kosong2.pop(0)
    print(m, end=' ')

    for neighbor in graph3[m]:
        if neighbor not in kosong:
            kosong.append(neighbor)
            kosong2.append(neighbor)


print()
kosong3 = []
kosong3.append(10)

while kosong3:
    m = kosong3.pop(0)
    print(m, end=' ')

# Berusaha untuk mengambil hikmah dari keseluruhan tu

# Implemetasi breadth first search pada dunia nyata
senin = {
    'cisco': ['jaringan', 'mikrotik', 'fortinet'],
    'jaringan': [],
    'mikrotik': ['python', 'javascript'],
    'fortinet': ['python'],
    'python': ['Compiler', 'Multiprocessing', 'Fungsi'],
    'Fungsi':[]
}
bfs(visited, queue, 'cisco')

# Lah kalau penggunaan node sendiri harus dengan menggunakan slices atau integer ya?, bukan dalam bentuk string.