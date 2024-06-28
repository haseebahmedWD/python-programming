import math

comp = complex(input("Enter a complex number: "))
if(comp.real > comp.imag):
    print("num real: ",comp.real)
else:
    print("num imaginary: ",comp.imag)