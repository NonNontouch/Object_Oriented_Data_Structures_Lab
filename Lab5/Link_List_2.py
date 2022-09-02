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
        return self.head.next == None

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