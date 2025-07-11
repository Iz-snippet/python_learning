a= int(input("enter your age :- "))

#if statement 1
if(a%2==0):
    print("the value is even")
#end of if statement 1

#if satement 2
if(a>18):
    print("your above age to consent.")
elif(a<0):
    print("please put a valid age:")
elif (a==0):
    print("your putting a zero")
else:
    print("your below age to consent.")

print("the program is end")

#end of if statement 2