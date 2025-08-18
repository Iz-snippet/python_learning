#Write a program to print third, fifth, and seventh element from a list using enumerate function.

l = [3, 513, 53, 535,78,89,8,44,5]

for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(item)
