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
            s += str(cur.data) + "->"
            cur = cur.next
        s += str(cur.data)
        return s

    def str_reverse(self):
        cur, s = self.tail.previous, ""
        if cur == self.head:
            return ""
        while cur.previous != self.head:
            s += str(cur.data)+"->"
            cur = cur.previous
        s += str(cur.data)
        return s

    def isEmpty(self):
        return self.head.next == self.tail

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

    def remove(self, data):
        t = self.head
        count=-1
        while t.next != self.tail:
            t = t.next
            count+=1
            if t.data == data:
                t.previous.next = t.next
                t.next.previous = t.previous
                del t
                return "removed : "+data+" from index : "+str(count)
        del t
        return "Not Found!"

    def printlinklist(self):
        print("linked list :", self.__str__())
        print("reverse :", self.str_reverse())


L = DoublyLinkedList()
inp = input('Enter Input : ').split(',')

for i in inp:
    i=i.replace(' ','')
    if i[:2] == "Ab":
        L.insert(0, i[2:])
        L.printlinklist()
    elif i[:1] == "A":
        L.append(i[1:])
        L.printlinklist()
    elif i[:1] == "I":
        index, data = i[1:].split(':')
        print(L.insert(index, data))
        L.printlinklist()
        del index, data
    elif i[:1] == "R":
        print(L.remove(i[1:]))
        L.printlinklist()
"""
Chapter : 5 - item : 2 - Doubly Linked List(append,insert,remove)
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
"""