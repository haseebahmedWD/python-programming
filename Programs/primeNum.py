#write a program to check a number is prime
#first method
"""
i = 2
flag = False
n = int(input("Enter a number: "))
while(i<n):
    if(n % i == 0):
        print(n,"is not prime")
        flag = True
        break
    else:
        i+=1
if(flag == False):
    print(n,"is prime")
"""

#second method using else with while loop
i = 2
n = int(input("Enter a number: "))
while(i<n):
    if(n % i == 0):
        print(n,"is not prime")
        break
    i+=1
else:
    print(n,"is prime")