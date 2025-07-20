# create a class programmer for storing information of few programmers working at microsoft

class programmer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin= pin

p= programmer("Ishake","12378900","700084")
print(p.name,p.salary,p.pin,p.company)
