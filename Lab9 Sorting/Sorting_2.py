def sortnotcareneggative(lst=[]):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] >= 0 and lst[j] >= 0 and lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


inp = input("Enter Input : ").split(' ')
inp = list(map(int, inp))
print(*sortnotcareneggative(inp))
"""
Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
"""