class Employee:
    lan="English"      
    salary="12000000"
    

    def getinfo(self):
        print(f"the language is {self.lan}. the salary is {self.salary}")


@staticmethod
def greet(self):
     print("Good Morning")


Ishake=Employee()
Ishake.lan="Javascript"      
print(Ishake.lan,Ishake.salary)
Ishake.getinfo()




