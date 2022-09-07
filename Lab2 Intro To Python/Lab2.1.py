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
