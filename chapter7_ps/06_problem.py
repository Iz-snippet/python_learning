# write a program to find factorial of given number using for loop 

n=int(input("Enter the Number:- "))
product=1
for i in range(1,n+1):
    product=product*i

print(f"the factorial of {n} is {product}")


