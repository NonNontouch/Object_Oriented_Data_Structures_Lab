class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class roughTree:
    def __init__(self):
        self.root = None

    def create_complete_tree(self, n, value):
        self.root = Node('*')
        queue = [self.root]
        temp_n = n
        n -= 1
        while True:
            node = queue.pop(0)

            if n > int(temp_n/2)+1:
                node.left = Node('*')
            else:
                node.left = Node(value.pop(0))
            n -= 1
            if n == 0:
                break
            queue.append(node.left)

            if n > int(temp_n/2)+1:
                node.right = Node('*')
            else:
                node.right = Node(value.pop(0))
            n -= 1
            if n == 0:
                break
            queue.append(node.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            if root.left and root.right:
                if root.left.data > root.right.data:
                    root.data = root.right.data
                else:
                    root.data = root.left.data
                root.left.data -= root.data
                root.right.data -= root.data

    def findsum(self, root,data):
        if root:
            data = self.findsum(root.left,data)
            data = self.findsum(root.right,data)
            data += root.data
        return data


inp = input("Enter Input : ").split('/')
inp[1] = inp[1].split()
inp[0], inp[1] = int(inp[0]), list(map(int, inp[1]))
tree = roughTree()
if (int(inp[0]/2))+1 != len(inp[1]):
    print("Incorrect Input")
    exit()
tree.create_complete_tree(inp[0], inp[1])
tree.postorder(tree.root)
print(tree.findsum(tree.root,0))


"""
Chapter : 8 - item : 2 - AVL ( Insert Only )
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว
** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
"""

"""
Chapter : 8 - item : 3 - ต้นไม้หยาบ
ต้นไม้หยาบเป็นต้นไม้แบบ Complete Binary Tree มีทั้งสิ้น N โหนด การเรียกชื่อโหนดจะเรียกเป็นโหนดที่ 1,2,3,... ไปเรื่อยๆจนถึงโหนดที่ N เริ่มต้นจะเติมค่าตั้งแต่โหนดที่ [N / 2] + 1 ไปจนถึงโหนดที่ N ต่อมาจะมีการขีดฆ่าต้นไม้หยาบ จากโหนดลูกสองโหนดใดๆที่อยู่ติดกัน โดยใช้หลักการว่าโหนดพ่อจะเอาค่าของโหนดลูกที่มีค่าน้อยที่สุดขึ้นมา แล้วลบค่าของโหนดลูกทั้งสองด้วยค่านั้น ให้นักศึกษาเขียนโปรแกรมเพื่อหาผลรวมโหนดภายหลังการขีดฆ่าต้นไม้หยาบ

โดย input จะแบ่เป็น 2 ฝั่งด้วย /
1. ด้านซ้ายจะเป็นจำนวนโหนด (N) โดยรับประกันว่ามีจำนวนโหนดอย่างต่ำที่สุดคือ 3
2. value จำนวน [N / 2] + 1 ค่า เป็นค่าตั้งแต่โหนดที่ [N / 2] + 1 จนถึง N และถ้าหากจำนวน value ไม่เท่ากับ [N / 2] + 1 จะแสดงผลลัพธ์เป็น "Incorrect Input"

หมายเหตุ ต้นไม้ในข้อนี้ไม่จำเป็นต้องเป็น Perfect Binary Tree แต่จำเป็นต้องมีจำนวนโหนดเป็นเลขคี่
"""
