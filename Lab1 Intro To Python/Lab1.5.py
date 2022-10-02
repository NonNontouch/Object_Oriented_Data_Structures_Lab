def strtolist(num):
    listnumstr = list(num.split())
    listnumint = []
    for n in listnumstr:
        listnumint.append(int(n))
    return listnumint


print("*** Fun with countdown ***")
num = input("Enter List : ")
numlist = strtolist(num)
i = 1
foundcounter = 0
ans = []
temp = []
if numlist[i-1] == 1:
    temp.append(1)
    ans.append(temp)
    foundcounter += 1
    temp = []
while i < len(numlist):
    if numlist[i] == 1 and numlist[i-1] != 2:
        temp.append(1)
        ans.append(temp)
        foundcounter += 1
        temp = []
    while numlist[i-1]-1 == numlist[i]:
        if numlist[i] == 1:
            temp.append(numlist[i-1])
            temp.append(numlist[i])
            ans.append(temp)
            foundcounter += 1
            break
        temp.append(numlist[i-1])
        i += 1
    temp = []
    i += 1

ans = [ans]
ans = [foundcounter, *ans]

print(ans)
"""
Chapter : 1 - item : 5 - Countdown มหาสนุก
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร
"""