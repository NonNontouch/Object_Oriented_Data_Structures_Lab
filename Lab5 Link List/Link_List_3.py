class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.previous = self.head

    def __str__(self):
        cur, s = self.head.next, ""
        if cur == self.tail:
            return ""
        while cur.next != self.tail:
            s += str(cur.data)+' '
            cur = cur.next
        s += str(cur.data)
        return s


    def append(self, data):
        p = Node(data)
        t = self.head
        while t.next != self.tail:
            t = t.next
        t.next = p
        p.previous = t
        p.next = self.tail
        self.tail.previous = p
        del p, t

    
    def insert(self, index, data):

        p = Node(data)
        t = self.head
        count = -1

        while t != self.tail:
            t = t.next
            count += 1
            if int(index) == count:
                p.previous=t.previous
                p.next=t
                t.previous.next=p
                t.previous=p                             
                return "index = "+str(index)+" and data = "+str(data)
        del p, t
        return "Data cannot be added"
    def size(self):
        t=self.head
        count = -1
        while t.next != self.tail:
            t = t.next
            count += 1
        if t.next == self.tail and count != -1:
            count+=1
        del t
        return count


LinkList=DoublyLinkedList()
l1, l2 = input("Enter Input (L1,L2) : ").split(' ')
l1 = [*l1.split("->")]
l2 = [*l2.split("->")]
print("L1    : ",end='')
for i in l1:
    LinkList.append(i)
    print(i,end=' ')
print()
print("L2    : ",end='')
j=0
for i in l2:
    tempsize=LinkList.size()
    LinkList.insert(tempsize-j,i)
    j+=1
    print(i,end=' ')

print()
print("Merge :",LinkList)
"""
Chapter : 5 - item : 3 - รวม Linked List
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง
"""