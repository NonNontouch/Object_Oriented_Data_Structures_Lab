def bi_search(l, h, arr, x):
    if l > h:
        return False
    else:
        mid = (l+h)//2
        if x == arr[mid]:
            return True
        #ข้อมูลอยู่ด้านขวา
        elif x > arr[mid]:
            return bi_search(mid+1, h, arr, x)
        #ข้อมูลอยู่ด้านซ้าย
        else:
            return bi_search(l, mid-1, arr, x)


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
"""
Chapter : 10 - item : 1 - หัดใช้ Binary Search
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา
"""
