#  Add a static method in problem 2 to greet the user with "hello".
# create a class programmer for storing information of few programmers working at microsoft

class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print (f"The cube is {self.n**3}")
    def SquareRoot(self):
        print(f"The squareroot is{self.n**0.5}")

    @staticmethod
    def greet():
        print("hello there !")  

a=calculator( int(input("enter the number:- ")))
a.greet()
a.square()
a.cube()
a.SquareRoot()
