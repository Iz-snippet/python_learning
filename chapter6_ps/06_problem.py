# write a program to calculate the grade of a student from his marks from the follwiong scheme
#  90-100:- Ex
# 80-90:- A
# 70-80:- B
# 60-70:- C
# 50-60:- D
# <50  :- F


marks= int(input("enter your marks:- "))

if(marks<=100 and marks>=90):
    print("you get  Ex grade ")
elif(marks<=90 and marks>=80):
    print("you get  A grade ")
elif(marks<=80 and marks>=70):
    print("you get  B grade ")
elif (marks<=70 and marks>=60):
    print("you get  C grade ")
elif(marks<=60 and marks>=50):
    print("you get  D grade ")
else:
    print("you are failed in the exam")
