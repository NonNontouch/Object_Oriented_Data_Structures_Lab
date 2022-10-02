def findMax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max = findMax(lst[1:])
    return max if max > lst[0] else lst[0]
inp = [int(x) for x in input("Enter Input : ").split(' ')]
print("Max :", findMax(inp))
"""
Chapter : 6 - item : 1 - หาค่ามากที่สุด

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

ให้เขียน Recursive หาค่า Max ของ Input
"""