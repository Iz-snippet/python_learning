# write a python program to find the greatest amoung four numbers enter by user

a1=int(input("enter the number 1:- "))
a2=int(input("enter the number 2:- "))
a3=int(input("enter the number 3:- "))
a4=int(input("enter the number 4:- "))

if(a1>a2 and a1>a3 and a1>a4):
    print("the greatest value amoung the four numbers is :",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("the greatest value amoung the four numbers is :",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("the greatest value amoung the four numbers is :",a3)
else:
    print("the geratest value amoung the four numbers is :",a4)
