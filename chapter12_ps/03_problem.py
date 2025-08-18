#Write a list comprehension to print a list which contains the multiplication table of a user entered number.
mylist=[1,2,9,3,4,5,6,7,8,9,10]
num=int(input("Enter a number of your choice:- "))
multiplication_table=[num*i for i in mylist]
print(multiplication_table)
