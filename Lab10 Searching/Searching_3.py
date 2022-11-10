class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, table, maxcol):
        self.table = [None for i in range(table)]
        self.maxcol = maxcol

    def hashing(self, inde, data):
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
                        print("Max of collisionChain")
                        break
        for i in range(len(self.table)):
            print("#{0}\t{1}".format(i+1, h.table[i]))

    def isfull(self):
        if self.table.count(None) == 0:
            return True
        else:
            return False


inp = input(" ***** Fun with hashing *****\nEnter Input : ").split('/')
table, maxcol = inp[0].split(' ')
table, maxcol = int(table), int(maxcol)
text = inp[1].split(',')
h = hash(table, maxcol)
for i in text:
    key, value = i.split(' ')
    if not h.isfull():
        h.hashing(sum([ord(i) for i in key]) % table, Data(key, value))
        print("---------------------------")
    else:
        print("This table is full !!!!!!")
        break
"""
Chapter : 10 - item : 3 - Fun with hashing
ให้น้องเขียน Hashing โดยมีการทำงานดังนี้
1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)
อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ
"""
