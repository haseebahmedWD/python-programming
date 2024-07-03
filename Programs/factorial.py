#write a program to calculate factorial
n = int(input("Enter a num: "))
temp = n
while(n>1):
    temp = temp * (n-1)
    n-=1
print("Factorial: ",temp)