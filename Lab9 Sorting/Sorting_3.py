def recur_insertion(lst, n):
    if n <= 0:
        return
    recur_insertion(lst, n-1)
    val = lst[n]
    j = n-1
    j = movenum(lst, j, val)
    lst[j+1] = val
    return j+1


def movenum(lst, j, val):
    if j < 0:
        return j
    if val < lst[j]:
        lst[j+1] = lst[j]
        j -= 1
        j = movenum(lst, j, val)
    return j


def insert(data):
    global sortedlist
    sortedlist.append(data)
    return recur_insertion(sortedlist, len(sortedlist)-1)


inp = input("Enter Input : ").split(' ')
inp = list(map(int, inp))
sortedlist = [inp.pop(0)]
for i in range(len(inp)):
    data = inp.pop(0)
    if len(inp) != 0:
        print("insert %d at index %d : %s %s" %
              (data, insert(data), sortedlist, inp))
    else:
        print("insert %d at index %d : %s " %
              (data, insert(data), sortedlist))
print("sorted\n", sortedlist, sep='')
"""
Chapter : 9 - item : 3 - insertion sort [recursive]
เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
"""
