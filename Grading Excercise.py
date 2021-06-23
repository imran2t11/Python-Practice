marks = []
#taking in the input for 5 marks from the user and adding it to the list
for i in range(5):
    marks.append(int(input()))
# now that we have all the marks we can just loop over it
output = ""
for i in marks:
    
    input=i
    if input>=90 :
        output+="A"
    elif input>=80 and input<90:
        output+="B"
    elif input>=70 and input<80:
        output+="C"
    elif input>=60 and input<70:
        output+="D"
    elif input>=50 and input<60:
        output+="E"
    else:
        output+="F"    
#Write your code here    
#for every mark concatenate grades to the output e.g output+="A"
    #start here

#now we simply print the output
print(output)
