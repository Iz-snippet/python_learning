# Write a class Calculator capable of finding square, cube, and squareroot of a number.

class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print (f"The cube is {self.n**3}")
    def SquareRoot(self):
        print(f"The squareroot is{self.n**0.5}")
        
a=calculator( int(input("enter the number:- ")))
a.square()
a.cube()
a.SquareRoot()

