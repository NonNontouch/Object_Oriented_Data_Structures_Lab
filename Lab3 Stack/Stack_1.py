class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.item = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def get_size(self):
        return len(self.items)


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()

for e in ls:

    s.push(e)

print(s.get_size(), "Data in stack : ", s.items)

while not s.isempty():

    s.pop()

print(s.get_size(), "Data in stack : ", s.items)
