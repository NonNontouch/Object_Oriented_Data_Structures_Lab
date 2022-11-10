class Data:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(self.key)


class hash:
    def __init__(self, table, maxcol, threshold):
        self.table = [None for i in range(table)]
        self.maxcol = maxcol
        self.treshold = threshold
        self.dataintable = 0

    def hashing(self, inde, data):
        if self.is_at_threshold():
            print("****** Data over threshold - Rehash !!! ******")
            self.rehashing()
            inde = data.key % len(h.table)
        if self.table[inde] == None:
            self.table[inde] = data
        else:
            i = 0
            for j in range(len(self.table)):
                inde_2 = (inde+(j*j)) % len(self.table)
                if self.table[inde_2] == None:
                    self.table[inde_2] = data
                    break
                elif i != self.maxcol:
                    print("collision number {0} at {1}".format(j+1, inde_2))
                    i += 1
                    if i == self.maxcol:
                        print("****** Max collision - Rehash !!! ******")
                        self.rehashing()
                        self.hashing(data.key % len(self.table), data)
                        return

    def rehashing(self):
        tempdata = []
        for i in range(len(self.table)-1, -1, -1):
            if self.table[i] != None:
                tempdata.append(self.table[i])
                self.table[i] = None
        temptable = [None for i in range(len(self.table), self.findprime(len(self.table)*2))]
        self.table = self.table+temptable
        for i in tempdata:
            self.hashing(i.key % len(self.table), i)

    def printtable(self):
        for i in range(len(self.table)):
            print("#{0}\t{1}".format(i+1, self.table[i]))
        print("----------------------------------------")

    def findprime(self, num):
        while not self.isprime(num):
            num += 1
        return num

    def isprime(self, num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def is_at_threshold(self):
        return True if (self.dataintable/len(self.table))*100 >= self.treshold else False


inp = input(" ***** Rehashing *****\nEnter Input : ").split("/")
table, maxcol, threshold = inp[0].split(' ')
table, maxcol, threshold = int(table), int(maxcol), int(threshold)
h = hash(table, maxcol, threshold)
text = list(map(int, inp[1].split(' ')))
print("Initial Table :")
h.printtable()
for i in text:
    h.dataintable += 1
    print("Add :", i)
    h.hashing(i % len(h.table), Data(i))
    h.printtable()
"""
Chapter : 10 - item : 4 - Rehashing
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด
หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 
และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11
การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision
อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
"""
