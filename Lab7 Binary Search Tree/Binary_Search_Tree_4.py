class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

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
                root.right.parent = root
            else:
                root.left = self.insert(val, root.left)
                root.left.parent = root
            return root

    def delete(self, data, node):
        if not node:
            return False
        if node.data < data:
            return self.delete(data, node.right)
        elif node.data > data:
            return self.delete(data, node.left)
        else:
            # Found Data
            succ = self.find_inorder_successor(node)
            if not succ:  # succ == None / node เป็น root หรือ node ที่ไม่มีลูก
                if node == self.root:
                    if self.root.left:
                        self.root = self.root.left
                        self.root.parent = None
                    elif self.root.right:
                        self.root = self.root.right
                        self.root.parent = None
                    else:
                        self.root = None
                else:
                    tempparent = node.parent
                    if tempparent.left == node:
                        tempparent.left = None
                    else:
                        tempparent.right = None
                return True
            # สลับdata
            node.data = succ.data
            # ลบnode succ
            tempparent = succ.parent
            if tempparent.left == succ:
                if succ.left:
                    tempparent.left = succ.left
                else:
                    tempparent.left = succ.right
            else:
                if succ.left:
                    tempparent.right = succ.left
                else:
                    tempparent.right = succ.right
            return True

    def find_inorder_successor(self, node):
        # กรณี1 มีตัวขวา suc คือตัวที่น้อยที่สุดในsub tree ขวา
        if node.right:
            return self.find_min(node.right)
        # กรณ2 ไม่มีตัวด้านขวาให้returnถือว่าไม่มี
        return None

    def find_min(self, node):
        cur = node
        while cur != None and cur.left != None:
            cur = cur.left
        return cur


def printTree90(node, level=0):
    if node != None:
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
        if tree.delete(int(i[2:]), tree.root):
            printTree90(tree.root)
        else:
            print("Error! Not Found DATA")
            printTree90(tree.root)
"""
Chapter : 7 - item : 4 - delete node in tree
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
โดยมีการป้อน input ดังนี้
i <int> = insert data
d <int> = delete data
หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว
"""
