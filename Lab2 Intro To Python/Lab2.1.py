class Calculator:

    ### Enter Your Code Here ###
    def __init__(self, num):
        self.num = num
    def __add__(self,num2):

        return int(self.num)+num2.num

    def __sub__(self,num2):

        return int(self.num)-num2.num

    def __mul__(self,num2):

        return int(self.num)*num2.num

    def __truediv__(self,num2):

       return float(self.num)/float(num2.num)
    


x, y = input("Enter num1 num2 : ").split(",")

x, y = Calculator(int(x)), Calculator(int(y))

print(x+y, x-y, x*y, x/y, sep="\n")
"""
Chapter : 2 - item : 1 - Simple OOP Calculator
จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

class Calculator :

    ### Enter Your Code Here ###

    def __add__(self):

        ###Enter Your Code For Add Number###

    def __sub__(self):

        ###Enter Your Code For Sub Number### 

    def __mul__(self):

        ###Enter Your Code For Mul Number###

    def __truediv__(self):

        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")
"""