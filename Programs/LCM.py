#Find the lcm of two numbers
i,j = 1,1
flag = False
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
#swap values 
if(a<b):
    a = a+b
    b = a-b
    a = a-b
#comparing the multiples of both numbers
while(i<=10):
    while(j<=10):
        if((a*i) == (b*j)):
            print(a*i)
            flag = True
            break
        j+=1
    if(flag == True):
        break
    i+=1
    j=1
    

