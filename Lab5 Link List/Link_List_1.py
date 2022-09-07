class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            del t
        del p

    def addHead(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            self.head = p
            self.head.next = t
            del t
        del p

    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return "Found"
            else:
                t = t.next
        del t
        return "Not Found"

    def index(self, item):
        t = self.head
        count = 0
        while t != None:
            if t.value == item:
                return count
            else:
                t = t.next
                count += 1
        del t, count
        return "-1"

    def size(self):
        t = self.head
        count = 0
        while t != None:
            count += 1
            t = t.next
        return count

    def pop(self, pos):
        t = self.head
        count = 0
        if pos == 0 and t != None:
            self.head = None
            return "Success"
        while t != None:
            if count == int(pos)-1:
                if t.next == None:
                    return "Out of Range"
                elif t.next.next == None:
                    t.next == None
                    return "Success"
                elif t.next.next != None:
                    t.next = t.next.next
                    return "Success"
            count += 1
            t = t.next
        del t, count
        return "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)