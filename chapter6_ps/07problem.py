# write a program to find out whether a given post is talking about "ishake" or not 

post=input("enter your post :-")
if("Ishake".lower() in post.lower()):
    print("this post is talking about ishake")
else:
    print("this post is not talking about ishake")

#use lower for comparison both in lower case also
