import keyword  #keyword.py is pre-defined module in python that contain keywords list
import sampleFile1 #sampleFile1.py is user-define module

print("There are",len(keyword.kwlist),"keywords in python")
print(keyword.kwlist)

print("x + y = ", sampleFile1.x + sampleFile1.y)

#arithmetic operators
# / is true division operator in python
#// is floor division operator and it is same like C language
print("3 / 4 = ", 3/4)
print("3 // 4 = ", 3//4)
print("3.0 // 4.0 = ", 3.0//4.0)

#logical operators examples
print("seeta" or "geeta")
print("seeta" and "geeta")
print(0 and 5)
print(0 or 5)

#assignment of multiple variables
e,f,g = 10,55,100
print("Values of e f g = ",e,f,g)

x = 5
y = 5
print("ID of x: ",id(x))
print("ID of y: ",id(y))
print("x is y:",x is y)

y = 6
print("ID of x: ",id(x))
print("ID of y: ",id(y))
print("x is y:",x is y)

#membership operators
values = "hello world"
print("values ",values)
print("world in values: ", "world" in values)

#input
print("Enter some text")
x = input()
print(x)
