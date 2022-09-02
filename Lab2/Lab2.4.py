def findfive():
    global num, temp, ans
    for i in range(0, len(num), 1):
        for j in range(i+1, len(num), 1):
            for k in range(j+1, len(num), 1):
                if num[i]+num[j]+num[k] == 5:
                    temp.append(num[i])
                    temp.append(num[j])
                    temp.append(num[k])
                    temp.sort()
                    ans.append(temp)
                    temp = []

def findduplicate():
    global ans,temp
    for i in ans:
        if i not in temp:
            temp.append(i)
    return temp

num = input("Enter Your List : ").split()
if len(num) < 3:
    print("Array Input Length Must More Than 2")
    exit()
num = [int(i) for i in num]
temp = []
ans = []
findfive()
ans=findduplicate()
print(ans)