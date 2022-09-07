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