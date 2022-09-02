def drawplus(x):
    for k in range(x):
        print("+", end='')

def drawdot(x):
    for j in range(x):
        print(".", end='')

def drawupper() :
    for i in range(num):
        drawdot(num-i-1)
        print("*", end='')
        drawplus((2*i)-1)
        if i != 0:
            print("*", end='')
        for j in range((num-i)*2-3):
            print(".", end='')
        if i != num-1:
            print("*", end='')
        drawplus((2*i)-1)
        if i != 0:
            print("*", end='')
        drawdot(num-i-1)
        print("")

def drawlower():
    for i in range((2*num)-2):
        drawdot(i+1)
        print("*", end='')
        drawplus((4*num)-(2*i)-7)
        if i != 2*num-3:
            print("*", end='')
        drawdot(i+1)
        print("")
print("*** Fun with Drawing ***")
num = input("Enter input : ")
num = int(num)
drawupper()
drawlower()