def addcomma(Number):
    return ("{:,}".format(Number))

print("*** Converting hh.mm.ss to seconds ***")
time = input("Enter hh mm ss : ")
h,m,s = [int(i) for i in time.split(" ")]
if h>=60 or h<0:
    print("hh(%d) is invalid!"%h)
elif m>=60 or m<0 :
    print("mm(%d) is invalid!"%m)
elif s>=60 or s<0 :
    print("ss(%d) is invalid!"%s)
else :
    ans=(h*3600)+(m*60)+s
    print("%.2d:%.2d:%.2d = %s seconds" %(h,m,s,addcomma(ans)))


