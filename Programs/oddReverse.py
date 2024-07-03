#write a program to print odd numbers in reverse order of given range
n = int(input("Enter a range: "))
while(n>0):
    if(n % 2 != 0):
        print(n,end=" ")
    n-=1

