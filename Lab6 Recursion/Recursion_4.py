def perketcalculation(L):
    if len(L) == 1 and len(L[0]) == 1:
        temp = list(map(int, L[0][0].split(' ')))
        return abs(temp[0]-temp[1])
    elif len(L) == 1 and len(L[0]) > 1:
        temp = morethanonecalculation(L[0])
        return abs(temp[0]-temp[1])
    diff = perketcalculation(L[1:])
    ismax = morethanonecalculation(L[0])
    ismax = abs(ismax[0]-ismax[1])
    return diff if diff < ismax else ismax

#หาซัปเซทของข้อมูลที่นำเข้ามา เพื่อหาเซทที่คำนวณแล้วจะได้มากที่สุด
def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

#ถ้าหากเซมของข้อมูลที่ส่งมาเป็นเซทที่มีมากกว่า 2 ให้ทำการloopคำนวณซ้ำ
def morethanonecalculation(L):
    if len(L) == 1:
        temp = list(map(int, L[0].split(' ')))
        s = temp[0]
        b = temp[1]
        return [s, b]
    result = morethanonecalculation(L[1:])
    temp = list(map(int, L[0].split(' ')))
    result[0] *= temp[0]
    result[1] += temp[1]
    return result


L = input("Enter Input : ").split(',')
print(perketcalculation(combs(L)[1:]))
"""
Chapter : 6 - item : 4 - Perket
“เปอร์เกต์” เป็นอาหารแสนอร่อยที่ใครๆก็รู้จักกัน และแน่นอนว่าส่วนผสมย่อมเป็นสิ่งที่ต้องพิถีพิถันอย่างยิ่ง

คุณมีส่วนผสมทั้งหมด N ชนิด แต่ละชนิดจะมีความเปรี้ยว S และความขม B เมื่อนำส่วนผสมมารวมกัน ความเปรี้ยว ลัพธ์ จะได้จากผลคูณของค่าความเปรี้ยวของทุกชนิดที่ใช้ 
ในขณะที่ความขมลัพธ์ จะได้จากผลบวกของความขมของ ทุกชนิดที่ใช้ ส่วนผสมที่ใช้นั้น

เปอร์เกต์ที่อร่อยที่สุดนั้น จะมีผลต่างค่าความเปรี้ยวลัพธ์และค่าความขมลัพธ์ของส่วนผสมทั้งหมดน้อยที่สุด และเรา จำเป็นต้องใช้ส่วนผสมอย่างน้อย 1 ชนิด

โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด



******* อธิบาย input

โดยส่วนผสมแต่ละชนิดจะแบ่งด้วย comma ( ' , ' ) โดยในแต่ละส่วนผสม จะมีจำนวนเต็มสองจำนวน S และ B คือค่าความเปรี้ยวและค่าความขมของ ส่วนผสมชนิดนั้น



******* รับประกันว่าสำหรับทุกข้อมูลนำเข้า เมื่อนำส่วนผสมทุกชนิดแล้ว จะได้ค่าความเปรี้ยวลัพธ์และความขมลัพธ์ ไม่เกิน 1,000,000,000
"""