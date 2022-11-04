inp = input("Enter Input : ").split(' ')
inp = list(map(int, inp))
flag = True
i = 1
while i < len(inp):
    if (inp[i] < inp[i - 1]):
        flag = False
        break
    i += 1
if flag:
    print("Yes")
else:
    print("No")
