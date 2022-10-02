print("*** multiplication or sum ***")
numstring = input("Enter num1 num2 : ") 
num1,num2 = [int(i) for i in numstring.split(" ")]
if num1*num2>1000 :
    print("The result is",num1+num2)
else :
    print("The result is",num1*num2)
"""
Chapter : 1 - item : 2 - multiplication or sum
รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้
show ผลคูณของจำนวนทั้งสอง
"""