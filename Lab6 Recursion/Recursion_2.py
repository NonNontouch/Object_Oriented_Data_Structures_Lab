def length(txt):
    global count
    temp = ''
    if txt == '':
        return ''
    if count % 2 == 0:
        temp = txt[0]+'*'
    else:
        temp = txt[0]+'~'
    count += 1
    return temp+length(txt[1:])


count = 0
print(length(input("Enter Input : ")),"\n"+str(count))
"""
Euclidean Algorithm
Chapter : 6 - item : 2 - Length of a String EXTRA

ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว
"""