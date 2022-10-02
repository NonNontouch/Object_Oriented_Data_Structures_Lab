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
"""
Chapter : 2 - item : 3 - Odd And Even
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

def odd_even(type, data, mode):
    //Code Here

โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List

Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา

Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่
"""