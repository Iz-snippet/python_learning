# write program to print the following star pattern:
# *
# **
# ***             for n=3

n=int(input("enter the number :- "))
for i in range(1,n+1):
    print("*"*(1*i),end="")
    print("")

