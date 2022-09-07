def find_gcd(a, b):
    if a < 0 or b < 0:
        a, b = abs(a), abs(b)
    elif b == 0:
        return a
    a -= int(a/b)*b
    if a == 0:
        return b
    b -= int(b/a)*a
    if b == 0:
        return a
    else:
        return find_gcd(a, b)


a, b = input("Enter Input : ").split(' ')
a, b = int(a), int(b)
if a == 0 and b == 0:
    print("Error! must be not all zero.")
    exit()
if b > a:
    temp = b
    b = a
    a = temp

print("The gcd of %d and %d is : %d" % (a, b, find_gcd(a, b)) if a >=
      0 or b >= 0 else "The gcd of %d and %d is : %d" % (b, a, find_gcd(a, b)))
