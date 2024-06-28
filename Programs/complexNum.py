import math

c = complex(input("Enter a complex number: "))
if(c.real > c.imag):
    print(c.real,">",c.imag)
else:
    print(c.imag,">",c.real)