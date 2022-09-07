print("*** multiplication or sum ***")
numstring = input("Enter num1 num2 : ") 
num1,num2 = [int(i) for i in numstring.split(" ")]
if num1*num2>1000 :
    print("The result is",num1+num2)
else :
    print("The result is",num1*num2)