a=int(input("Hi Ishake, Enter a number:- "))
b=int(input("Enter a second number:- "))
if (b==0):
    raise ZeroDivisionError("Hey, our program is not meant to divide by zero.")
else:
    print(f"the division a/b is {a/b}")