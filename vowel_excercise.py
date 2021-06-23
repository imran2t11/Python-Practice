text1 =  input()
text2 = input()
for text in [text1,text2]:
    #just iterating through them
    #Write your code here. for each text you have to print("YES") or print("NO") as described in the problem
    if("a" in text) and ("e" in text) and ("i" in text) and ("o" in text)and ("u" in text) :
        print ("YES")
    else:
        print("NO")