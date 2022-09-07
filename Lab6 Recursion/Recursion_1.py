def findMax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max = findMax(lst[1:])
    return max if max > lst[0] else lst[0]
inp = [int(x) for x in input("Enter Input : ").split(' ')]
print("Max :", findMax(inp))
