class Employee:
    a=1
class programmer(Employee):
    b=2
class manager(programmer):
    c=3


o=Employee()
print(o.a)# prints the atrrib
#print(o.b) #shows an eror as there is no b attribute in Employee class

o=programmer()
print (o.b,o.a)

o=manager()
print(o.c,o.b,o.a)