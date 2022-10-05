def length(txt):
    temp = ''
    if txt == '':
        return ''
    if find_len(txt) % 2 == 0:
        temp = txt[0]+'*'
    else:
        temp = txt[0]+'~'
    return temp+length(txt[1:])

def find_len(txt):
    if txt=="":
        return 0
    else:
        count=find_len(txt[1:])+1
    return count
inp = input("Enter Input : ")
print(length(inp),"\n"+str(find_len(inp)))
"""
Euclidean Algorithm
Chapter : 6 - item : 2 - Length of a String EXTRA

ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว
"""