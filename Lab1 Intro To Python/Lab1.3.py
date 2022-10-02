print("*** Reading E-Book ***")
Text = input("Text , Highlight : ")
UseText,wantedtext = Text.split(",")
for i in range(len(UseText)) :
    if UseText[i] == wantedtext :
        print("[%c]"%wantedtext,end="")
    else :
        print("%c"%UseText[i],end="")
"""
Chapter : 1 - item : 3 - Reading E-book
กฤษฎากำลังอ่านหนังสืออิเล็กทรอนิกส์เพื่อเตรียมสอบอยู่ในห้องสมุดของโรงเรียนชื่อดังประจำจังหวัดแห่งหนึ่ง แล้วก็มีความคิดผุดหนึ่งขึ้นมาในหัวของกฤษฎา
ถ้าหากสามารถ Auto Highlight คำที่ต้องการจาก Text ได้ก็คงจะดีไม่น้อย แต่กฤษฎาไม่รู้จะทำอย่างไรดี กฤษฎาจึงอยากจะไหว้วานคุณให้ช่วยเขียนโปรแกรมในการ
Highlight Text แบบที่กฤษฎาต้องการ
"""