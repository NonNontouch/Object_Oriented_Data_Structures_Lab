class Queue:
    def __init__(self, items=None):
        if items == None:
            self.items = []
        else:
            self.items = items
        self.bomb = []
        self.count = 0
        self.countbombfail = 0

    def enQueue(self, i):
        self.items.append(i)

    def dequeue(self, index=None):
        if self.size() == 0:
            return None
        elif index == None:
            return self.items.pop(0)
        else:
            return self.items.pop(index)

    def isempty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def getbomb(self):
        if len(self.bomb) != 0:
            return self.bomb.pop(0)

    def findtripletext(self):
        bombplace = False
        for i in range(2, len(self.items), 1):
            if self.items[i-2] == self.items[i-1] == self.items[i]:
                if len(self.bomb) != 0:
                    self.items.insert(i, self.bomb.pop(0))
                    bombplace = True
                if self.items[i-2] == self.items[i-1] == self.items[i]:
                    for j in range(i, i-3, -1):
                        self.dequeue(j)
                    if bombplace:
                        bombplace = False
                        self.countbombfail += 1
                        self.count-=1
                    self.count += 1
                    return


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.bomb = []
        self.count = 0

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def get_size(self):
        return len(self.items)

    def findbomb(self):

        for i in range(self.get_size()-3, -1, -1):
            if self.items[i] == self.items[i+1] == self.items[i+2]:
                for i in range(2):
                    self.pop()
                self.bomb.append(self.pop())
                self.count += 1
                return


Normal, Mirror = input("Enter Input (Normal, Mirror) : ").split(' ')
Normal = [*Normal]
Mirror = [*Mirror]
Mirror.reverse()
Normalqueue = Queue()
Mirrorqueue = Stack()
for i in Mirror:
    Mirrorqueue.push(i)
    Mirrorqueue.findbomb()
Normalqueue.bomb = Mirrorqueue.bomb
for i in Normal:
    Normalqueue.enQueue(i)
    Normalqueue.findtripletext()
print("NORMAL :")
if Normalqueue.size() == 0:
    print("0")
    print("Empty")
else:
    print(Normalqueue.size())
    Normalqueue.items.reverse()
    print(*Normalqueue.items, sep='')
print(Normalqueue.count, "Explosive(s) ! ! ! (NORMAL)")
if Normalqueue.countbombfail != 0:
    print("Failed Interrupted", Normalqueue.countbombfail, "Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
if Mirrorqueue.get_size() == 0:
    print("0")
    print("ytpmE")
else:
    print(Mirrorqueue.get_size())
    Mirrorqueue.items.reverse()
    print(*Mirrorqueue.items, sep='')
print("(RORRIM) ! ! ! (s)evisolpxE", Mirrorqueue.count)
