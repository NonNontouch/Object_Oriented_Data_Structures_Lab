class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        # stack[0]จะเป็น rootgเมื่อสิ้นสุดinput
        self.stack = []

    def insert(self, data):
        if data in ['+', '-', '*', '/']:
            a = self.stack.pop()
            b = self.stack.pop()
            c = Node(data)
            c.left = b
            c.right = a
            self.stack.append(c)
            return
        self.stack.append(Node(data))

    def infixread(self, node, infix=[]):
        # inorder_reading
        if node:
            if node.data in  ['+', '-', '*', '/']:
                infix.append('(')
            infix = self.infixread(node.left,infix)
            infix.append(node.data)
            infix = self.infixread(node.right,infix)
            if node.data in  ['+', '-', '*', '/']:
                infix.append(')')
        return infix
    def prefixread(self,node,prefix=[]):
        #preorder read
        if node:
            prefix.append(node.data)
            prefix = self.prefixread(node.left,prefix)
            prefix = self.prefixread(node.right,prefix)
        return prefix
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input("Enter Postfix : ")
tree = BST()
for i in inp:
    tree.insert(i)
print("Tree :")
tree.printTree(tree.stack[0])
print("--------------------------------------------------")
print("Infix : ",*tree.infixread(tree.stack[0]),sep='')
print("Prefix : ",*tree.prefixread(tree.stack[0]),sep='')

"""
Chapter : 7 - item : 5 - Expression Tree
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /
"""
