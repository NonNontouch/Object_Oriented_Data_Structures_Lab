class Van:
    def __init__(self, day, VanNum):
        self.day = day
        self.VanNum = VanNum


def fixList(Tree, son):
    if son <= 0:
        return
    dad = (son-1)//2
    if Tree[dad].day > Tree[son].day:
        Temp = Tree[dad]
        Tree[dad] = Tree[son]
        Tree[son] = Temp
        fixList(Tree, dad)
    else:
        return


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if (l < n and arr[l].day < arr[largest].day):
        largest = l
    if (r < n and arr[r].day < arr[largest].day):
        largest = r
    if (largest != i):
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        heapify(arr, n, largest)


def getMinHeap(arr):
    global n
    lastElement = arr[n - 1]
    arr[0] = lastElement
    n = n - 1
    heapify(arr, n, 0)


K, command = input('Enter Input : ').split('/')
van = [x for x in range(1, int(K)+1)]
command = [int(i) for i in command.split()]
useing_car = []
for i in range(len(command)):
    day = command[i]
    if len(van) == 0:
        while useing_car[0].day != 0:
            for v in useing_car:
                v.day -= 1
        while useing_car[0].day == 0:
            temp = useing_car[0]
            n = len(useing_car)
            getMinHeap(useing_car)
            useing_car.pop()
            van.append(temp.VanNum)
            if len(useing_car) == 0:
                break
        van.sort()
    car = van.pop(0)
    useing_car.append(Van(day, car))
    if len(useing_car) != 1:
        fixList(useing_car, len(useing_car)-1)
    print("Customer %d Booking Van %d | %d day(s)" % (i+1, car, command[i]))


"""Chapter : 8 - item : 5 - จองรถตู้
บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลขจำนวนเต็มบวกตั้งแต่ 1 จนถึง K ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า 
ลูกค้าจะต้องทำการจองรถตู้ก่อน โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้ จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน  ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 
รถตู้ที่มีหมายเลข 5 จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ สำหรับการจองแต่ละครั้ง ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด
  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
-  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
-  ฝั่งขวาเป็น customer จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา"""
