#tuple 
#declaration and initialization
t1 = (10,20,30,40,50)
t2 = (44,)
print(t1)
#print(type(t1))

#user input
#in the line below first we split elements with white spaces and get list of string values
#after that we convert these string values to integer
#in the last we save all values in tuple container

t1 = tuple(int (x) for x in input("Enter tuple elements: ").split(" "))
print(type(t1))
print(t1)
print('\n')

#build in methods
print('Sorted tuple: ',sorted(t1))
print('Sorted tuple (reverse): ',sorted(t1,reverse=True))
print('Sum tuple: ',sum(t1))
print('\n')

#printing
for x in t1:
    print(x)
print('\n')

#slicing operator
print(t1)
print('Slicing: ')
print('t1[2::1]',t1[2 : : 1])
print('t1[::-1]',t1[ : : -1])