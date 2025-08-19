# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of the same numbers.


table=[str(7*i) for i in range(1,11)]
s="\n".join(table)
print(s)