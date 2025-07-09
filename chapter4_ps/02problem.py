# write program to store marks of a six student and display them in a sorted manner

marks=[]

m1=int(input("enter the marks: "))
marks.append(m1)

m2=int(input("enter the marks: "))
marks.append(m2)

m3=int(input("enter the marks: "))
marks.append(m3)

m4=int(input("enter the marks: "))
marks.append(m4)

m5=int(input("enter the marks: "))
marks.append(m5)

m6=int(input("enter the marks: "))
marks.append(m6)

marks.sort()
print("the sorted list of marks for six students is ",marks)