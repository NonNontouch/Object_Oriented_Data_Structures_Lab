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

    def peek(self):
        return self.items[-1]

    def isempty(self):
        return self.items == []

    def get_size(self):
        return len(self.items)


def match(open, close):
    openbrackets = "([{"
    closebrackets = ")]}"
    return openbrackets.index(open) == closebrackets.index(close)


def findmatch(instr):
    s = Stack()
    i = 0
    error = 0
    while i < len(instr) and error == 0:
        c = instr[i]
        if c in '{[(':
            s.push(c)
        elif c in '}])':
            if s.get_size() > 0:
                if not match(s.pop(), c):
                    error = 1
            else:
                error = 2
        i += 1
    if s.get_size() > 0 and error == 0:
        error = 3
    return error, c, i, s


instr = input("Enter expresion : ")
err, c, i, s = findmatch(instr)
if err == 1:
    print(instr, "Unmatch open-close")
elif err == 2:
    print(instr, "close paren excess")
elif err == 3:
    print(instr, "open paren excess  ", s.get_size(), ': ', end='')
    for ele in s.items:
        print(ele, sep=' ', end='')
else:
    print(instr, "MATCH")
