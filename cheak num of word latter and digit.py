numofletter=0
numofdigit=0
numofword=0
text=input("Enter Your Text :")

for j in text:
    j=j.lower()
    if j >="a" and j <= "z":
        numofletter=numofletter+1
    elif j >= "0" and j <= "9":
        numofdigit=numofdigit+1
    elif j== ' ':
        numofword=numofword+1
print("Number Of Letter",numofletter)
print("Number Of Digit :",numofdigit)
print("Number Of Word :",numofword+1)