class Queue:
    def __init__(self, items=None, diff=None):
        if items == None:
            self.items = []
            self.outcode = []
            self.diff = diff
        else:
            self.items = items
            self.outcode = []
            self.diff = diff

    def enQueue(self, i):
        self.outcode.append(i)

    def dequeue(self):
        if self.size() != 0:
            return self.items.pop(0)
        else:
            return None

    def decode(self):
        for i in self.items:
            self.enQueue(chr(ord(i)+self.diff))
            print(self.outcode)

    def isempty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


code, hint = input("Enter code,hint : ").split(",")
code=[*code]
diff = ord(hint)-ord(code[0])
Q = Queue(code, diff)
Q.decode()
