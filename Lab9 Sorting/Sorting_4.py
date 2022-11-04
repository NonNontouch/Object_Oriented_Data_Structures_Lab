def insertionSort(arr):
    global inp
    for i in range(1, len(arr)):
        key = arr[i]
        key2 = inp[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            inp[j+1] = inp[j]
            j -= 1
        arr[j + 1] = key
        inp[j+1] = key2
    return inp


inp = input("Enter Input : ").split(' ')
listtosort = []
for i in inp:
    for j in i:
        jascii = ord(j)
        if (jascii >= 65 and jascii <= 90) or (jascii >= 97 and jascii <= 122):
            listtosort.append(jascii)
print(*insertionSort(listtosort))
"""
Chapter : 9 - item : 4 - Sort by alphabet
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่
a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
"""