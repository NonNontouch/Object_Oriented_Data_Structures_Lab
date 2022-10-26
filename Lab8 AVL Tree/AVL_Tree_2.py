
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)


class AVL:

    def __init__(self):
        self.root = None

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, data, root):
        if not root:
            return Node(data)
        else:
            if root.data <= data:
                root.right = self.insert(data, root.right)
            else:
                root.left = self.insert(data, root.left)

        root.height = 1+max(self.__getheight(root.left),
                            self.__getheight(root.right))
        balance = self.__isbalance(root)

        if balance > 1:
            if data < root.left.data:
                # Case 1 - เบี้ยวซ้ายทั้งหมด
                return self.__rightRotate(root)
            else:
                # Case 2 - พ่อเบี้ยวซ้าย ลูกเบี้ยวขวา
                root.left = self.__leftRotate(root.left)
                return self.__rightRotate(root)
        elif balance < -1:
            if data >= root.right.data:
                # Case 3 - เบี้ยวขวาทั้งหมด จะมีกรณีที่dataเหมือนกันจึงต้องใส่ =
                return self.__leftRotate(root)
            else:
                # Case 4 - พ่อเบี้ยวขวา ลูกเบี้ยวซ้าย
                root.right = self.__rightRotate(root.right)
                return self.__leftRotate(root)
        return root

    def __getheight(self, node):
        if not node:
            return 0
        return node.height

    def __isbalance(self, node):
        if not node:
            return 0
        return self.__getheight(node.left)-self.__getheight(node.right)

    def __rightRotate(self, px):
        py = px.left
        px.left = py.right
        py.right = px
        px.height = 1 + max(self.__getheight(px.left),
                            self.__getheight(px.right))
        py.height = 1 + max(self.__getheight(py.left),
                            self.__getheight(py.right))
        return py

    def __leftRotate(self, px):
        py = px.right
        px.right = py.left
        py.left = px
        px.height = 1 + max(self.__getheight(px.left),
                            self.__getheight(px.right))
        py.height = 1 + max(self.__getheight(py.left),
                            self.__getheight(py.right))
        return py


inp = input("Enter Input : ").split(' ')
tree = AVL()
for i in inp:
    print(f"Insert : ( {i} )")
    tree.root = tree.insert(int(i), tree.root)
    tree.printTree(tree.root)
    print("--------------------------------------------------")

"""
Chapter : 8 - item : 2 - AVL ( Insert Only )
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว
** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
"""
