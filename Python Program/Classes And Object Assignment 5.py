# Design a class ‘Complex ‘with data members for real and imaginary part. Provide default and
# Parameterized constructors. Write a program to perform arithmetic operations of two complex
# numbers

class Complex:
    def __init__(self,c1=2+3j,c2=3+2j):
         self.complexnumber1=c1
         self.complexnumber2=c2
    def addition(self):
        self.add=self.complexnumber1+self.complexnumber2
        print("Addition of Complex Number:",self.add)
    def substraction(self):
        self.sub=self.complexnumber1-self.complexnumber2
        print("Substraction of Complex Number:",self.sub)
    def multiplication(self):
        self.mul=(self.complexnumber1)*(self.complexnumber2)
        print("Multiplication of Complex Number:",self.mul)
    def division(self):
        self.div =(self.complexnumber1)/(self.complexnumber2)
        print("Division of Complex Number:", self.div)

print("Arithmetic Operation of Two Complex Number".center(80,"*"))
c1=Complex(c1=4+2j)
c1.addition()
c1.substraction()
c1.multiplication()
c1.division()