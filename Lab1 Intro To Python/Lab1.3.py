print("*** Reading E-Book ***")
Text = input("Text , Highlight : ")
UseText,wantedtext = Text.split(",")
for i in range(len(UseText)) :
    if UseText[i] == wantedtext :
        print("[%c]"%wantedtext,end="")
    else :
        print("%c"%UseText[i],end="")
    
