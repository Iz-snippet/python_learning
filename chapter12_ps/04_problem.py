#Store the multiplication tables generated in Problem 3 in a file named Tables.

mylist=[1,2,9,3,4,5,6,7,8,9,10]
num=int(input("Enter a number of your choice:- "))
multiplication_table=[num*i for i in mylist]
with open('tables.txt','w') as f:
    f.write(f" the table of {num} is : {(multiplication_table)}+ \n")
