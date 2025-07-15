# write a python program to find greates amoung three numbers by using function


def fg(a1,a2,a3):
    
   if(a1>a2 and a1>a3):
        return(f"{a1}is greatest")
   elif(a2>a1 and a2>a3):
        return(f"{a2}is greatest")
   else:
        return(f"{a3} is greatest")

print(fg(4,5,6))


    
