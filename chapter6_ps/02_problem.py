# write a program to find out whether a student 
# is pass or fail, if it  requires total 40% and at least 33%, in each subject to pass
# assume subjects and take marks as an input from the User

marks1=int(input ("enter the marks :- "))
marks2=int(input ("enter the marks :- "))
marks3=int(input ("enter the marks :- "))

#check for total percentage

total_percentage= (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass the exam.",total_percentage)
else:
    print("you failed, better luck next time",total_percentage)
