class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not self.root:
            self.root = Node(val)
        elif not root:
            return Node(val)
        else:
            if root.data <= val:
                root.right = self.insert(val, root.right)
            else:
                root.left = self.insert(val, root.left)
            return root

    def delete(self, data, node):
        if not node:
            print("Error! Not Found DATA")
            return None
        if node.data < data:
            node.right = self.delete(data, node.right)
        elif node.data > data:
            node.left = self.delete(data, node.left)
        else:
            # Found Data
            if node.left and node.right:
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.data, cur.data = cur.data, node.data
                node.right = self.delete(data, node.right)
            elif node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                return None
        return node


def printTree90(node, level=0):
    if node:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    if i[0] == 'i':
        print("insert", i[2:])
        tree.insert(int(i[2:]), tree.root)
        printTree90(tree.root)
    elif i[0] == 'd':
        print("delete", i[2:])
        tree.root = tree.delete(int(i[2:]), tree.root)
        printTree90(tree.root)

"""
Chapter : 7 - item : 4 - delete node in tree
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
โดยมีการป้อน input ดังนี้
i <int> = insert data
d <int> = delete data
หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว
"""
