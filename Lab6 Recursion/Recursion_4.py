def perketcalculation(L):
    if len(L) == 1:
        s, b = 1, 0
        for j in L[0]:
            tempj = list(map(int, j.split(' ')))
            s *= tempj[0]
            b += tempj[1]
        return abs(s-b)
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
