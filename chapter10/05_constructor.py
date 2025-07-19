class Employee:
    lan="English"      
    salary="12000000"
    
    def __init__(self, name,lan,salary):
        self.name=name
        self.salary=salary
        self.lan=lan
        print("I am creating an object")

    def getinfo(self):   # a dunder method which can automaticlly called
        print(f"the language is {self.lan}. the salary is {self.salary}")

    def greet(self):
        print("Good Morning")


Ishake=Employee("Ishake","JavaScript","1300000000000000")
# Ishake.name="Ishake"      
print(Ishake.name,Ishake.lan,Ishake.salary)
Ishake.getinfo()
Ishake.greet() 




