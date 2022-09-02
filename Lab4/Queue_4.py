class Queue:
    def __init__(self, myqueue=None, yourqueue=None):
        if myqueue != None and yourqueue != None:
            self.myqueue = myqueue
            self.yourqueue = yourqueue

        else:
            self.myqueue = []
            self.yourqueue = []
        self.score = 0

    def enmyqueue(self, i):
        self.myqueue.append(i)

    def enyourqueue(self, i):
        self.yourqueue.append(i)

    def demyqueue(self):
        if self.mysize() != 0:
            return self.myqueue.pop(0)
        else:
            return None

    def deyourqueue(self):
        if self.yoursize() != 0:
            return self.yourqueue.pop(0)
        else:
            return None

    def mysize(self):
        return len(self.myqueue)

    def yoursize(self):
        return len(self.yourqueue)

    def printacrivity(self):
        activity = ["Eat", "Game", "Learn", "Movie"]
        location = ["Res.", "ClassR.", "SuperM.", "Home"]
        print("My   Activity:Location = ", end='')
        for i in range(0, self.mysize(), 1):
            mytemp = [int(x) for x in self.myqueue[i].split(":")]
            print(activity[mytemp[0]], end=':')
            if i != self.mysize()-1:
                print(location[mytemp[1]], end=", ")
            else:
                print(location[mytemp[1]])
        print("Your Activity:Location = ", end='')
        for i in range(0, self.yoursize(), 1):
            yourtemp = [int(x) for x in self.yourqueue[i].split(":")]
            print(activity[yourtemp[0]], end=':')
            if i != self.yoursize()-1:
                print(location[yourtemp[1]], end=", ")
            else:
                print(location[yourtemp[1]])
        del mytemp, yourtemp, activity, location

    def calculatescore(self):
        for i in range(0, self.mysize(), 1):
            mytemp = self.myqueue[i].split(':')
            yourtemp = self.yourqueue[i].split(':')
            if mytemp[0] == yourtemp[0] and mytemp[1] != yourtemp[1]:
                self.score += 1
            elif mytemp[0] != yourtemp[0] and mytemp[1] == yourtemp[1]:
                self.score += 2
            elif mytemp[0] == yourtemp[0] and mytemp[1] == yourtemp[1]:
                self.score += 4
            else:
                self.score -= 5
        del mytemp, yourtemp

    def frindornot(self):
        if self.score >= 7:
            print("Yes! You're my love! : Score is", self.score, end='.')
        elif self.score >= 0:
            print("Umm.. It's complicated relationship! : Score is",
                  self.score, end='.')
        else:
            print("No! We're just friends. : Score is", self.score, end='.')


queue = input("Enter Input : ").split(',')
Q = Queue()
for i in queue:
    temp = i.split(' ')
    Q.enmyqueue(temp[0])
    Q.enyourqueue(temp[1])
print("My   Queue = ", end='')
print(*Q.myqueue, sep=', ')
print("Your Queue = ", end='')
print(*Q.yourqueue, sep=', ')
Q.calculatescore()
Q.printacrivity()
Q.frindornot()
