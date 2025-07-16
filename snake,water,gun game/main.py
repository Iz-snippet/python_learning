# lets suppose 
# -1 for water
# 1 for snake
# 0 for gun
import random

computer= random.choice([-1,0,1])   #entering the choiche of the computer

youstr=input("enter your choice:- ")   #entering the choiche of the user
youdict={"snake":1, "water":-1,"gun":0}           #creating a dictionary
you=youdict[youstr]                      # listing my choices from the dictionary
reversedict={1:"snake", -1:"water",0:"gun"} # ceating reverse for choices for computer
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(you==computer):
    print("this match is tie")                   #match draw
else:                                            #match condtions
    if(computer==-1 and you==1):
      print("You Win")
    elif(computer==-1 and you==0):
      print("You Lose")
    elif (computer==1 and you==-1):
      print("You Lose")
    elif (computer==1 and you==0):
      print("You Win")
    elif (computer==0 and you==-1):
      print("You Win")
    elif (computer==0 and you==1):
      print("You Lose")
    else:
      print("something went wrong")
    