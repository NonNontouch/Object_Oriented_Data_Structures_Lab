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

    def insert(self, data,root):
        #recursion version
        if root == None :
            return Node(data)
        else :
            if root.data <= data:
                root.right = self.insert(data,root.right)
            else:
                root.left = self.insert(data,root.left)
            return root
    def findlower(self,root,data,ls):
        #Inorder
        if root!=None:
            ls = self.findlower(root.left,data,ls)
            if root.data<data:     
                ls.append(root.data)
            ls = self.findlower(root.right,data,ls)
        return ls
        
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        


T = BST()
inp = input("Enter Input : ").split('|')
inp[0] = [int(i) for i in inp[0].split()]
root = None
for i in inp[0]:
    root = T.insert(i,root)
T.printTree(root)
print("--------------------------------------------------")
print("Below %d : "%(int(inp[1])),end='')
ls=T.findlower(root,int(inp[1]),[])
if ls!=[]:
    print(*ls)
else:
    print("Not have")
"""
Chapter : 7 - item : 2 - หาค่า Below
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree
***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
"""