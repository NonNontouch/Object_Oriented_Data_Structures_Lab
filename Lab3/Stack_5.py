

class Stack:
    def __init__(self, slotlen=None, slot=None,  operation=None, carnum=None):
        self.gorslotlen = slotlen
        if slot != [0]:
            self.__gorslot = slot  # ก
        else:
            self.__gorslot = []
        self.korslot = []  # ข
        self.operation = operation
        self.carnum = carnum

    def gorpush(self, i):  # ก
        self.__gorslot.append(i)

    def gorpop(self):  # ก
        return self.__gorslot.pop()

    def korpush(self, i):  # ข
        self.korslot.append(i)

    def korpop(self):  # ข
        return self.korslot.pop()

    def __arriveoperation(self):
        if len(self.__gorslot) < self.gorslotlen and self.carnum not in self.__gorslot:
            print("car", self.carnum, "arrive! : Add Car", self.carnum)
            self.gorpush(self.carnum)
        elif self.carnum in self.__gorslot:
            print("car", self.carnum, "already in soi")
        else:
            print("car", self.carnum, "cannot",
                  self.operation, ": Soi Full")
        print(self.__gorslot)

    def __departoperation(self):
        if len(self.__gorslot) != 0 and self.carnum in self.__gorslot:
            print("car", self.carnum, "depart ! : Car",
                  self.carnum, "was remove")
            for i in range(len(self.__gorslot)-1, -1, -1):
                if self.__gorslot[i]==self.carnum:
                    self.gorpop()
                    break
                self.korpush(self.gorpop())
            for i in range(len(self.korslot)-1, -1, -1):
                self.gorpush(self.korpop())
        elif len(self.__gorslot) == 0:
            print("car", self.carnum, "cannot depart : Soi Empty")
        else:
            print("car", self.carnum, "cannot depart : Dont Have Car", self.carnum )
        print(self.__gorslot)

    def dooperation(self):
        if self.operation == "arrive":
            self.__arriveoperation()
        else:
            self.__departoperation()


print("******** Parking Lot ********")
m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
m, n = int(m), int(n)
s = [int(x) for x in s.split(",")]
S = Stack(m, s, o, n)
S.dooperation()
