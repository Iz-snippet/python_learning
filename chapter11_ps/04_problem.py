#Write a class Vector representing a vector of n dimension. Overload the + and * operators which calculate the sum and the dot product of them

class Complex:
    def __init__(self, r,i):
        self.r=r
        self.i=i

    def  __add__(self,c2):
        return Complex(self.r+c2.r,self.i+c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)
