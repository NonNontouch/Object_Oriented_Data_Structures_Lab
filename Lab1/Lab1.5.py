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
