class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.combo = 0

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isempty(self):
        if self.items == []:
            print("Empty")
        else:
            for i in range(len(self.items)-1, -1, -1):
                print(self.items[i], end="")
            print("")

    def get_size(self):
        return len(self.items)

    def findtripletext(self):
        for i in range(2, len(self.items), 1):
            if self.items[i-2] == self.items[i-1] == self.items[i]:
                for j in range(3):
                    self.pop()
                self.combo += 1

    def iscombo(self):
        if self.combo > 1:
            print("Combo :", self.combo, "! ! !")


inp = input('Enter Input : ').split()
S = Stack()
for i in inp:
    S.push(i)
    S.findtripletext()
print(S.get_size())
S.isempty()
S.iscombo()
