print("*** Odd Even ***")
SorL, Text, OddorEven = input("Enter Input : ").split(",")
if SorL == 'S':
    if OddorEven == "Even":
        for i in range(1, len(Text), 2):
            print(Text[i], end="")
    elif OddorEven == "Odd":
        for i in range(0, len(Text), 2):
            print(Text[i], end="")
elif SorL == 'L':
    ans = []
    Text = [*Text.split(" ")]
    if OddorEven == "Even":
        for i in range(1, len(Text), 2):
            ans.append(Text[i])
    elif OddorEven == "Odd":
        for i in range(0, len(Text), 2):
            ans.append(Text[i])
    print(ans)
