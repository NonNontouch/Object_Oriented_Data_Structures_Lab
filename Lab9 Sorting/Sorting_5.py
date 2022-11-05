def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def n_length_combo(lst, n):

    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):
        # หยิบตัวที่น้อยที่สุดออกก่อน
        m = lst[i]
        remLst = lst[i + 1:]
        # ส่งตัวที่เหลือไปหา combo
        remainlst_combo = n_length_combo(remLst, n-1)
        # นำตัวที่น้อยที่สุดเอามารวมกับ combo ที่ได้หามา
        for p in remainlst_combo:
            l.append([m, *p])

    return l


def findcomb(lst):
    ans = []
    for i in range(1, len(lst)+1):
        ans = ans + n_length_combo(lst, i)
    return ans


def findlist(num, lst):
    ans = []
    for i in lst:
        if num == sum(i):
            ans.append(insertionSort(i))
    return ans


num, lst = input("Enter Input : ").split('/')
lst = list(map(int, lst.split(' ')))
lst = insertionSort(lst)
lst = findcomb(lst)
lst = findlist(int(num), lst)
if lst == []:
    print("No Subset")
    exit()
print(*lst, sep='\n')
"""
Chapter : 9 - item : 5 - Sort Subset
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /
1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม
โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้
1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก
ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import
อธิบาย Test Case 1:
[2]
[-1, 3]
[0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]
"""