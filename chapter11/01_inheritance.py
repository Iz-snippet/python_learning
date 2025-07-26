class Employee:
    company="ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary} ")

# insted of doing this 
# class programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary} ")

#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language}")

class programmer(Employee):
    company ="ITC Infotech"
    def showlanguage(self):
         print(f"the name is {self.name} and he is good with {self.language}")




a=Employee()
b=programmer()

print(a.company,b.company)