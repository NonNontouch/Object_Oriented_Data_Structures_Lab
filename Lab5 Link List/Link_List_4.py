class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail

    def __str__(self):
        cur, s = self.head.next, ""
        if cur == self.tail:
            return ""
        while cur.next != self.tail:
            s += str(cur.data) + "->"
            cur = cur.next
        s += str(cur.data)
        return s

    def append(self, data):
        p = Node(data)
        t = self.head
        while t.next != self.tail:
            t = t.next
        t.next = p
        p.next = self.tail
        del p, t

    def set_next(self, index1, index2):
        index1, index2 = int(index1), int(index2)
        t = self.head
        count1 = -1
        while t != self.tail:
            t = t.next
            count1 += 1
            if count1 == index1 and t != self.tail:
                p = self.head
                count2 = -1
                while p != self.tail:
                    p = p.next
                    count2 += 1
                    if count2 == index2 and p != self.tail:
                        t.next = p
                        return "Set node.next complete!, index:value = "+str(count1)+':'+str(t.data)+\
                        " -> "+str(count2)+':'+str(p.data)
                self.append(index2)
                return "index not in length, append : "+str(index2)
        if count1 == 0:
            return "Error! {list is empty}"
        return "Error! {index not in length}: "+str(index1)

    def find_loop(self):
        one_hop = self.head
        two_hop = self.head
        if one_hop.next == self.tail:
            return "No Loop\nEmpty"
        while True:
            one_hop = one_hop.next
            if two_hop.next != self.tail:
                two_hop = two_hop.next.next
            else:
                return "No Loop\n"+self.__str__()
            if one_hop == self.tail or two_hop == self.tail or two_hop == None:
                return "No Loop\n"+self.__str__()
            if one_hop == two_hop:
                return "Found Loop"


inp = input("Enter input : ").split(',')
linklist = DoublyLinkedList()
for i in inp:
    if i[:1] == 'A':
        linklist.append(i[2:])
        print(linklist)
    elif i[:1] == 'S':
        temp = i[2:].split(':')
        print(linklist.set_next(temp[0], temp[1]))
print(linklist.find_loop())
