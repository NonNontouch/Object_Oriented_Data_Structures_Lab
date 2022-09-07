class Queue:
    def __init__(self, items=None):
        if items == None:
            self.items = []
            self.cashier1 = []
            self.cashier2 = []
        else:
            self.items = items

    def enQueueitem(self, i):
        self.items.append(i)

    def enQueuecashier1(self, i):
        self.cashier1.append(i)

    def enQueuecashier2(self, i):
        self.cashier2.append(i)

    def dequeueitems(self):
        if self.itemsize() != 0:
            return self.items.pop(0)
        else:
            return None

    def dequeuecashier1(self):
        if self.cashier1size != 0:
            return self.cashier1.pop(0)
        else:
            return None

    def dequeuecashier2(self):
        if self.cashier2size != 0:
            return self.cashier2.pop(0)
        else:
            return None

    def isitemempty(self):
        return len(self.items) == 0

    def itemsize(self):
        return len(self.items)

    def cashier1size(self):
        return len(self.cashier1)

    def cashier2size(self):
        return len(self.cashier2)


Q = Queue()
count2 = 0
inp = [*input("Enter people : ")]
for i in inp:
    Q.enQueueitem(i)
for i in range(1, len(Q.items)+1):
    if (i-1) % 3 == 0 and Q.cashier1size() != 0:
        Q.dequeuecashier1()
    if Q.cashier2size() != 0:
        if count2 == 1:
            Q.dequeuecashier2()
            count2 = -1
        count2 += 1
    if Q.cashier1size() < 5:
        Q.enQueuecashier1(Q.dequeueitems())
    elif Q.cashier2size() < 5:
        Q.enQueuecashier2(Q.dequeueitems())
    
    print(i, Q.items, Q.cashier1, Q.cashier2)
