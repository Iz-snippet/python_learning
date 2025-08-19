#Write a program to filter a list of numbers which are divisible by 5.
def divisble5(n):
    if n%5==0:
        print("the number is divisble by 5")
    else:
        print("the number is not divisble by 5")

a=[10,20,30,44,50,60,70,80,90,100]

f=list(filter(divisble5,a))
print(f)
