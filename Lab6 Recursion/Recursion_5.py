def asteroid_collision(asts):  # parameter ห้ามเกิน 2 ตัว
    if len(asts) == 1:
        return asts
    ans = asteroid_collision(asts[1:])  # ให้ไล่จากตัวท้ายสุด
    anslen=len(ans)
    if anslen>0 and asts[0] > 0 and ans[0] < 0:  # ชนกัน
        if asts[0] == abs(ans[0]):  # ขนาดเท่ากัน
            if anslen > 1:
                return ans[1:]
            else:
                return []
        elif asts[0] < abs(ans[0]): #ขนาดไม่เท่ากัน ตัวหลังใหญ่กว่า
            return ans
        # ส่งตัวต่อไปของansไปเช็คเพื่อดูว่าจะชนอีกหรือเปล่า
        elif asts[0] > abs(ans[0]):
            return asteroid_collision([asts[0]]+ans[1:])
    else:  # ไม่ชน
        return [asts[0]]+ans


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
"""
Chapter : 6 - item : 5 - ดาวเคราะห์น้อย

นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def asteroid_collision(asts):
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))
"""