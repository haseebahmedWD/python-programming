#list is a iterable which is mutable. It can grow. It can contain hetrogenous/multiple data type values

l1 = [10,20,30,40,50]
l2 = [True,10,44.5,3+4j,'hello']
#display list
print(l1)
#display list1 using loop
for x in l1:
    print(x,end=' ')
print('\n')
#display list2 using loop
for x in l2:
    print(x,end=' ')
print('\n')

#negative indexing
print(l1)
print("l1[0]=",l1[0], "l1[-5]=", l1[-5])
print("l1[1]=",l1[1], "l1[-4]=", l1[-4])
print("l1[2]=",l1[2], "l1[-3]=", l1[-3])
print("l1[3]=",l1[3], "l1[-2]=", l1[-2])
print("l1[4]=",l1[4], "l1[-1]=", l1[-1])

#deleting a value
print(l1)
del l1[2]
print("after deleting l1[2]: ",l1)

#append()
l1.append(30)
print("after appending: ",l1)

#insert()
l1.insert(1,90)
l1.insert(50,140)
print(l1)