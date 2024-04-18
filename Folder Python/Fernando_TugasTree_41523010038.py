class TreeNode:
    def __init__ (self,data):
        self.data = data
        self.children = []

# Contoh penggunaan Tree
root = TreeNode("A")
root.children.append(TreeNode("B"))
root.children.append(TreeNode("C"))
root.children[0].children.append(TreeNode("D"))