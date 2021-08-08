class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        complex_self = complex(self.real, self.imaginary)
        complex_other = complex(other.real, other.imaginary)
        return complex_self + complex_other

    def __mul__(self, other):
        complex_self = complex(self.real, self.imaginary)
        complex_other = complex(other.real, other.imaginary)
        return complex_self * complex_other

a = complex(1, 2)
b = complex(2, 3)

print(a*b)