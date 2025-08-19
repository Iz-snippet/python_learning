# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

l=[10,20,30,44,50,60,70,80,90,100]

def greater(a, b):
    if (a>b):
        return a 
    return b

print(reduce(greater, l))