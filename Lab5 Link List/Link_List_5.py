class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


def createLL(LL):
    head = Node(LL[0])
    t = head
    for i in range(1, len(LL), 1):
        t.next = Node(LL[i])
        t = t.next
    return head


def printLL(head):
    t = head
    S = ""
    while t != None:
        S += str(t)+" "
        t = t.next
    del t
    return S


def SIZE(head):
    t = head
    count = 0
    while t != None:
        count += 1
        t = t.next
    return count


def scarmble(head, b, r, size):
    head = BottomUp(head, b, size)
    head, count = Riffle(head, r, size)
    head = Deriffle(head, r, count, size)
    head = Debottomup(head,size,b)


def BottomUp(head, b, size):
    t = head
    p = head

    for i in range(0, int((size*b)/100)-1, 1):
        t = t.next
    while p.next != None:
        p = p.next
    p.next = head
    head = t.next
    t.next = None
    print("BottomUp %.3f %% : %s" % (b, printLL(head)))
    return head


def Riffle(head, r, size):
    t = head
    p = head
    n = int((size*r)/100)
    for i in range(0, n-1, 1):
        t = t.next
    temp = t.next
    t.next = None
    t = temp
    while t != None and p != None:
        tempprevious = p
        temp = p.next
        p.next = t
        t = t.next
        p = p.next
        p.next = temp
        p = temp
    if t != None:
        tempprevious.next.next = t
    print("Riffle %.3f %% : %s " % (r, printLL(head)))
    return head, n


def Deriffle(head, r, count, size):
    t = head
    p = head.next
    phead = head.next
    if size-count > count:
        j = count
    elif size-count <= count:
        j = size-count
    n = 1
    while n != j:
        t.next = t.next.next
        t = t.next
        p.next = p.next.next
        p = p.next
        n += 1
    if size-count > count:
        t.next = phead

    elif size-count <= count:
        temp = p.next
        p.next = None
        t.next = temp
        while t.next != None:
            t = t.next
        t.next = phead
    print("Deriffle %.3f %% : %s" % (r, printLL(head)))
    return head


def Debottomup(head, size, b):
    t = head
    p = head

    for i in range(0, size-int((size*b)/100)-1, 1):
        t = t.next
    while p.next != None:
        p = p.next
    p.next=head
    head = t.next
    t.next=None
    print("Debottomup %.3f %% : %s"%(b,printLL(head)))
    return head

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split(' '))
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)

"""
Chapter : 5 - item : 5 - Scramble

เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

***** รูปแบบ input *****

แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน

2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****

***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    # Code Here

def printLL(head):
    # Code Here

def SIZE(head):
    # Code Here

def scarmble(head, b, r, size):
    # Code Here

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
"""