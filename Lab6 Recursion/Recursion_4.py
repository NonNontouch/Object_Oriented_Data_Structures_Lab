def perketcalculation(L):
    if len(L) == 1 and len(L[0]) == 1:
        temp = list(map(int, L[0][0].split(' ')))
        return abs(temp[0]-temp[1])
    elif len(L) == 1 and len(L[0]) > 1:
        temp = calculatemorethanone(L[0])
        return abs(temp[0]-temp[1])
    diff = perketcalculation(L[1:])
    ismax = calculatemorethanone(L[0])
    ismax = abs(ismax[0]-ismax[1])
    return diff if diff < ismax else ismax


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs


def calculatemorethanone(L):
    if len(L) == 1:
        temp = list(map(int, L[0].split(' ')))
        s = temp[0]
        b = temp[1]
        return [s, b]
    result = calculatemorethanone(L[1:])
    temp = list(map(int, L[0].split(' ')))
    result[0] *= temp[0]
    result[1] += temp[1]
    return result


L = input("Enter Input : ").split(',')
print(perketcalculation(combs(L)[1:]))
