# write a python program to find greates amoung three numbers

def fg():
    
   a1=int(input("Enter the number :- "))
   a2=int(input("Enter the number :- "))
   a3=int(input("Enter the number :- "))

   if(a1>a2 and a1>a3):
        print(f"{a1}is greatest")
   elif(a2>a1 and a2>a3):
        print(f"{a2}is greatest")
   else:
        print(f"{a3} is greatest")

fg()


    