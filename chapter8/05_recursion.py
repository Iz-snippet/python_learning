# simple factorial-rule
# factorial(n)= n*factorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)


n=int(input("enter the number :- "))
print(f"the Factorial of this is:- {factorial(n)}")