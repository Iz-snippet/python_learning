class Employee:
    def __init__(self) -> None:
        print("constructor of Employee")
    a=1
class programmer(Employee):
    def __init__(self) -> None:
        print("constructor of programmer")
    b=2
class manager(programmer):
    def __init__(self) -> None:
        super().__init__()
        print("constructor of Manager")
    c=3


o=Employee()
print(o.a)

o=programmer()
print (o.b,o.a)

o=manager()
print(o.c,o.b,o.a)