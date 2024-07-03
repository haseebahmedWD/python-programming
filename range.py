#range is a interator which is immutable mean its value cannot change
# we traverse range from start to end
# it contains Only integer values
#write a program to print square of natural numbers using range
num = int(input("Enter number range: "))
for x in range(1,num+1):
    print(x*x)

#print range values with single argument
#start = 0 step = 1 by default
r = range(5)
for x in r:
    print(x, end=" ")
print('\n')

r = range(2,10,2)
for x in r:
    print(x, end=" ")
print('\n')

r = range(10,3,-2)
for x in r:
    print(x, end=" ")
print('\n')