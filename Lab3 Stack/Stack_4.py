class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def get_size(self):
        return len(self.items)


j = -1
treecounter = 0
temphighesttree = 0
S = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == 'A':
        temp = i.split(" ")
        S.push(int(temp[1]))
        j += 1
        temp = []
    elif i == 'B' and j != -1:
        for i in range(len(S.items)-1, -1, -1):
            if temphighesttree < S.items[i]:
                temphighesttree = S.items[i]
                treecounter += 1
        print(treecounter)
        treecounter = 0
        temphighesttree = 0
    elif i == 'B' and j == -1:
        print("0")
