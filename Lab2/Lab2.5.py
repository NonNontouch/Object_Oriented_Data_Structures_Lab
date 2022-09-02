class funString():

    def __init__(self, string=""):

        self.string = string

    def size(self):
        return len(self.string)

    def changeSize(self):
        temp = ""
        for i in range(0, len(self.string)):
            asciichar = ord(self.string[i])
            if asciichar >= 65 and asciichar <= 90:
                temp += chr(asciichar+32)
            elif asciichar >= 97 and asciichar <= 122:
                temp += chr(asciichar-32)
        return temp

    def reverse(self):
        restring = ""
        for i in range(len(self.string)-1, -1, -1):
            restring += self.string[i]
        return restring

    def deleteSame(self):
        temp = "".join(dict.fromkeys(self.string))
        return temp


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)


if str2 == "1":
    print(res.size())

elif str2 == "2":
    print(res.changeSize())

elif str2 == "3":
    print(res.reverse())

elif str2 == "4":
    print(res.deleteSame())