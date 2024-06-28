#Write a program to calculate simple interest
amount = int(input("Enter principle amount: "))
r = int(input("Enter interest rate: "))
y = int(input("Enter total number of years: "))
roi = float(r /100)
SI = amount * roi * y
print("Simple interest is: ",SI)