class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, root):
        # recursion version
        if self.root == None:
            self.root = Node(data)
        elif root == None:
            return Node(data)
        else:
            if root.data <= data:
                root.right = self.insert(data, root.right)
            else:
                root.left = self.insert(data, root.left)
            return root

    def multbythree(self, root, data):
        if root != None:
            self.multbythree(root.left, data)
            if root.data > data:
                root.data *= 3
            self.multbythree(root.right, data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input("Enter Input : ").split('/')
inp[0] = [int(i) for i in inp[0].split()]
for i in inp[0]:
    T.insert(i, T.root)
T.printTree(T.root)
print("--------------------------------------------------")
T.multbythree(T.root, int(inp[1]))
T.printTree(T.root)

"""
Chapter : 7 - item : 2 - หาค่า Below
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree
***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
"""
