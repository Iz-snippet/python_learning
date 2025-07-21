# Create a class with a class attribute a; 
# create an object from it and set a directly using object: a = 0. Does this change the class attribute?

class demo:
    a=4

o=demo()
print(o.a) # prints the class  atrribute because instance atrribute is not here
o.a=0
print(o.a) #prints the instance attribute because instance attribute is here now

print(demo.a) # its doesnot effect the class attribute
