#Robert Roche
#CS172-Lecture-A, Lab-062

import math
class complex:

    def __init__(self,x,y):         #initializes the complex number with x being the real part, and y being the imaginary part
        self.x = x
        self.y = y

    def __str__(self):              #overrides string method
        a = (self.getReal(),self.getImaginary())
        return a

    def __add__(self, other):       #overrides addition method, and uses the formula given to calculate the real and imaginary parts
        if type(other)!= complex:   #if it is a normal number it is converted to complex number
            other = complex(other,0)
        num1 = self.getReal()+other.getReal()
        num2 = self.getImaginary()+other.getImaginary()
        return complex(num1,num2)

    def __sub__(self, other):       #overrides subtraction method, and uses the formula given to calculate the real and imaginary parts
        num1 = self.getReal() - other.getReal()
        num2 = self.getImaginary() - other.getImaginary()
        return complex(num1, num2)

    def __mul__(self, other):       #overrides multiplication method, and uses the formula given to calculate the real and imaginary parts
        num1 = (self.getReal()*other.getReal())-(self.getImaginary()*other.getImaginary())
        num2 = (self.getReal()*other.getImaginary())+(self.getImaginary()*other.getReal())
        return complex(num1,num2)

    def __abs__(self):              #overrides abolute value method, and uses the formula given to find the absolute value of the number
        return math.sqrt(self.getReal()**2+self.getImaginary()**2)

    def getReal(self):              #returns the real part of the number(accessor)
        return self.x

    def getImaginary(self):         #returns the imaginary part of the number(accessor)
        return self.y