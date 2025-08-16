#Write a class complex to represent complex numbers dimension .overload the + and * operator which calculate the sum and the dot product of them

class Complex:
    def __init__(self, r, i):
        self.r = r  # real part
        self.i = i  # imaginary part

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"


# Example usage
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
