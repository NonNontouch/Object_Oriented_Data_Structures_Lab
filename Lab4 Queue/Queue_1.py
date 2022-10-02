class Queue:
    def __init__(self, items=None):
        if items == None:
            self.items = []
        else:
            self.items = items

    def enQueue(self, i):
        self.items.append(i)

    def dequeue(self):
        if self.size() != 0:
            return self.items.pop(0)
        else:
            return None

    def isempty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


Q = Queue()
inp = input("Enter Input : ").split(',')
for i in inp:
    if i[0] == 'E':
        tempE = i.split(' ')
        Q.enQueue(int(tempE[1]))
        print(Q.size())
        tempE = []
    elif i[0] == 'D':
        tempD = Q.dequeue()
        if tempD != None:
            print(tempD, "0")
        else:
            print("-1")
if Q.size()!=0:
    for i in Q.items:
        print(i,end=' ')
else:
    print("Empty")

"""
Chapter : 4 - item : 1 - รู้จักกับ QUEUE
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา
E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

D  ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty
"""