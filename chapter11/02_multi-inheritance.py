class Employee:
    company="ITC"
    name="Ishake"

    def show(self):
        print(f"the name is {self.name} and the salary is {self.company} ")


class coder:
    language="python"
    def printLanguages(self):
        print(f"out of all the languages here is your language:{self.language}")


class programmer(Employee,coder):
    company ="ITC Infotech"
    def showlanguage(self):
         print(f"the name is {self.company} and he is good with {self.language}")




a=Employee()
b=programmer()

b.show()
b.showlanguage()
b.printLanguages()