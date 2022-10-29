class Node:

    def __init__(self, data, count, left=None, right=None):
        self.data = data
        self.count = count
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Huffman:

    def __init__(self):
        self.root = None

    def insert(self, node, data, count):
        if not node:
            return Node(data, count)
        elif count < node.count:
            node.left = self.insert(node.left, data, count)
        elif count == node.count:
            if data < node.data:
                node.left = self.insert(node.left, data, count)
            else:
                node.right = self.insert(node.right, data, count)
        elif count > node.count:
            node.right = self.insert(node.right, data, count)
        return node

    def in_order(self, node):
        if not node:
            return []

        s = self.in_order(node.right)\
            + [Node(node.data, node.count)]\
            + self.in_order(node.left)

        return s

    def inorderread(self, node):
        if node != None:
            self.inorderread(node.right)
            print(node.data, node.count, sep=' ', end='  ')
            self.inorderread(node.left)


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def printCode(node, code):
    s = ''
    if node:
        s = printCode(node.right, code + '1')
        if node.data != '*':
            s += "'" + str(node.data) + "': '" + code + "'"
        a = printCode(node.left, code + '0')
        if a != '':
            s += ', ' + a
    return s


def search(node, data, code):
    if not node:
        return None

    if data == node.data:
        return code
    if node:
        s = search(node.right, data, code + '1')
        if s != None:
            return s
        s = search(node.left, data, code + '0')
        return s


inp = list(input('Enter Input : '))
s = set(inp)
huff = Huffman()
for i in s:
    #สร้าง Tree ของข้อมูล
    huff.root = huff.insert(huff.root, i, inp.count(i))
#อ่านข้อมูลแบบ inorder เพื่อให้เรียงจากมากไปน้อย
data = huff.in_order(huff.root)
#นำตัวที่น้อยทีสุดออกมา
treelist = [data.pop()]

while len(data) != 0 or len(treelist) != 1:
    if len(treelist) > 1:
        #หากพบว่า ตัวสุดท้ายของ data มากกว่าหรือเท่ากับ data ที่popมา
        if data == [] or (data[-1].count >= treelist[0].count + treelist[1].count):
            #สร้าง node * 
            a, b = treelist.pop(0), treelist.pop(0)
            treelist.append(Node('*', a.count + b.count, a, b))
        else:
            treelist.append(data.pop())
    else:
        treelist.append(data.pop())

print('{' + f'{printCode(treelist[0], "")}' + '}')
printTree(treelist[0])
print('Encoded! : ', end='')
for key in inp:
    print(search(treelist[0], key, ''), end='')
"""

Chapter : 8 - item : 1 - Huffman Encoding

ให้นักศึกษาเขียนโปรแกรมในการเข้ารหัส Huffman (บีบอัดข้อมูล) โดยใช้ Tree และแสดงผลตามตัวอย่าง

#อ่านวิธีการเข้ารหัสได้ที่ http://datastructurealgori.blogspot.com/2017/06/huffmans-code.html"""
