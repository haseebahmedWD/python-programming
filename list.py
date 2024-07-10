#list is a iterable which is mutable. It can grow. It can contain heterogenous/multiple data type values

l1 = [10,20,30,40,50] 
l2 = [True,10,44.5,3+4j,'hello']  #heterogenous list

#display list
print(l1)

#display list1 using loop
for x in l1:
    print(x,end=' ')
print('\n')

#display list2 using loop
for x in l2:
    print(x,end=' ') #end='' is a keyword argument
print('\n')

#negative indexing
print(l1)
print("l1[0]=",l1[0], "l1[-5]=", l1[-5])
print("l1[1]=",l1[1], "l1[-4]=", l1[-4])
print("l1[2]=",l1[2], "l1[-3]=", l1[-3])
print("l1[3]=",l1[3], "l1[-2]=", l1[-2])
print("l1[4]=",l1[4], "l1[-1]=", l1[-1])
print('\n')

#deleting a value
print(l1)
del l1[2]
print("after deleting l1[2]: ",l1)
print('\n')

#append()
l1.append(30)
print("after appending 30: ",l1)
print('\n')

#insert()
print('insert(1,90)')
l1.insert(1,90)
print('insert(50,140)') 
l1.insert(50,140) #element will be inserted at last index  
print(l1)
print('\n')

#packing and unpacking of list
print('UnPacking of list')
l1 = [11,22,33]
print(l1)
a,b,c = l1
print('a=',a,'b=',b,'c=',c)
print('Packing of list')
a = 66
b = 77
c = 99
print('a=',a,'b=',b,'c=',c)
l1 = [a,b,c]
print(l1)
print("\n")

#List method list()
print("List method list() it only contain at least one iterable as argument")
l1 = list("hello world")
print(l1)
print('\n')

#comparison of lists
print('Comparison of lists')
l1 = [1,2,3,4,5]
l2 = [10,5,4,23,43]
l3 = [1,2,3,4,5]
print('l1 = ',l1)
print('l2 = ',l2)
print('l3 = ',l3)
print('l1 == l2: ',l1 == l2)
print('l1 > l2 : ',l1 > l2)
print('l1 < l2 : ',l1 < l2)
print('l1 == l3: ',l1 == l3)
print('\n')
#Concatenation of lists
print('Concatenation of lists')
print('l1 + l2:',l1+l2)
l1+=l3
print('l1 = l1 + l3:',l1)
print('\n')

#Repetition Operator
print('Repetition operator')
l1 = [11,22,33]
print('l1=',l1)
print("l1 * 3:",l1*3)
print('\n')

#List of List
print('List of list (2D-List)')
l1= [[1,2,3],[4,5,6],[7,8,9]]
print(l1,'\n')
#printing the 2-D array
i = 0
j = 0
while(i<3):
    while(j<3):
        print(l1[i][j],sep='   ',end=' ')
        j+=1
    print('\n')
    i+=1
    j=0
print('\n')

#List functions
print("List functions")
l1 = [10,20,30,40,40,50,60,70]
#remove()
print(l1)
print('l1.remove(40): ')    #it will remove the first occurance
l1.remove(40)
print(l1)
print('\n')

#pop()
print(l1)
x = l1.pop()
print('l1.pop():')
print(x)
print(l1)
print('\n')

#clear()
print(l1)
print('l1.clear()')
l1.clear()
print(l1)
print('\n')

#reverse()
l1 = [10,20,30,40,50,60,70]
print(l1)
print('l1.reverse()')
l1.reverse()
print(l1)
print('\n')

#index()
l1 = [10,20,30,40,50,60,70]
print(l1)
print('l1.index(40): ',l1.index(40))
print('l1.index(70): ',l1.index(70))
#if-else single line
x = (l1.index(50) if 50 in l1 else'50 is not in list l1')
print('l1.index(50): ',x, '\n')


#count()
l1 = [10,20,30,40,40,50,60,60,60,70]
print(l1)
print('l1.count(40): ',l1.count(40))
print('l1.count(10): ',l1.count(10))
print('l1.count(60): ',l1.count(60))
print('\n')

#sort() function of list class
print("sort() function of list class! \n(It sort the original list) \n")
l1 = [45,66,1,545,0,37,128]
print(l1)
l1.sort()
print('l1.sort()')
print(l1,'\n')

#list comprehension
#[expression  for  x  in  iterable]
#create a list of first n odd natural numbers
print('List comprehension')
print("Example1")
print([x**2 for x in range(2,10,2)])
print('\n')

print('Example2')
num = int(input("Enter range: "))
r = range(1,num+1)
oddNum = [(2*x)-1 for x in r]
print(oddNum,'\n')



