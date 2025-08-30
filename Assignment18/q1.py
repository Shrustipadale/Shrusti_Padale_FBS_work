class Complex:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag

    def __str__(self):
        return f"{self.real}+{self.imag}i"
    
    def __add__(self,c2):
        c3=Complex()
        c3.real=self.real+c2.real
        c3.imag=self.imag+c2.imag
        return c3
c1=Complex(2,3)
c2=Complex(3,4)
print(c1)
print(c2)

c3=c1+c2
print(c3)

