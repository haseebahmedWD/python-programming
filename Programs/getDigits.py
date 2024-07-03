#write a program to get digits from input and their sum
ipt = input("Enter a string (a-z,A-Z,0-9): ")
sum = 0
for x in ipt:
    if(ord(x) >=48 and ord(x) <=57):
        print(x, end=" ")
        sum+=int(x)
print("Sum of digits: ",sum)
