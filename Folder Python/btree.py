class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                    # Orde pohon
        self.keys = []                # Daftar kunci di node
        self.children = []            # Daftar anak dari node
        self.leaf = leaf              # Menunjukkan apakah node adalah daun

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[-1].traverse()

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)

    def insert_non_full(self, k):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            while i >= 0 and self.keys[i] > k:
                i -= 1
            if len(self.children[i + 1].keys) == 2 * self.t - 1:
                self.split_child(i + 1)
                if k > self.keys[i + 1]:
                    i += 1
            self.children[i + 1].insert_non_full(k)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self):
        if self.root:
            self.root.traverse()
            print()

    def search(self, k):
        return self.root.search(k) if self.root else None

    def insert(self, k):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, False)
            s.children.append(r)
            s.split_child(0)
            self.root = s
            s.insert_non_full(k)
        else:
            r.insert_non_full(k)


# Contoh penggunaan B-Tree dengan orde 3
btree = BTree(3)

# Memasukkan elemen ke dalam B-Tree
for item in [10,230,14,13,54,135,63,52,62,24,6]:
    btree.insert(item)

# Menampilkan elemen di B-Tree secara in-order
print("Traversal B-Tree: ")
btree.traverse()

# Mencari elemen
key = 20
found = btree.search(key)
print(f"\nKey {key} {'found' if found else 'not found'} in B-Tree.")
