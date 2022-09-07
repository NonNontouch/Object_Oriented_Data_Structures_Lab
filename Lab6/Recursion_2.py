def length(txt):
    global count
    temp = ''
    if txt == '':
        return ''
    if count % 2 == 0:
        temp = txt[0]+'*'
    else:
        temp = txt[0]+'~'
    count += 1
    return temp+length(txt[1:])


count = 0
print(length(input("Enter Input : ")),"\n"+str(count))
