def perketcalculation(L):
    if  len(L) == 1:
        s, b = 1, 0
        for j in L[0]:
            tempj = list(map(int, j.split(' ')))
            s *= tempj[0]
            b += tempj[1]
        return abs(s-b)
    diff = perketcalculation(L[1:])
    
    s, b = 1, 0
    for j in L[0]:
        tempj = list(map(int, j.split(' ')))
        s *= tempj[0]
        b += tempj[1]
    ismax = abs(s-b)
    return diff if diff < ismax else ismax


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs


L = input("Enter Input : ").split(',')
print(perketcalculation(combs(L)[1:]))
