#set is a class
#set is mutable
#set cannot have duplicate values
#set cannot have values in sequential order like other iterables(List,string,range)
#set cannot have indexing
#set cannot have slicing operator

#creating a set
s1 = {10,20,30,40,50,}
print("set: ",s1)
s1 = {} #it is not an empty set it is type dict
print("set {} = ",s1,type(s1))
print('\n')

s1 = set()  #it is empty set
print('s1 = set()',type(s1))
print('It is empty set')
print('\n')

#user input a list and remove its duplicate values
l1 = list(set(int(x) for x in input("Enter a list with duplicate values: ").split(' ')))
print(l1)
print('\n')

#Set object methods
#add() can add non-iterable or iterable values
print('add()')
s1={10,20,30,40}
print(s1)
s1.add(50) #it can take only one argument
print('s1.add(50) = ',s1)
s1.add((60,70,80))
print('s1.add(60,70,80) = ',s1) #adding a tuple, it add like an element
print('\n')

#update()
#update() can take only iterable values and more than one iterable values
#iterable elements become part of set as multiple values
print('update()')
print(s1)
s1.update((90,100))
print('s1.update(90,100) = ',s1)
s1.update((110,120),(130,140))
print('s1.update((110,120),(130,140)) = ',s1)
print('\n')

#remove()
#if element not existed then it will give error
print('remove()')
print(s1)
print('s1.remove(10)')
s1.remove(10)
print(s1)
# print('s1.remove(70)')
# s1.remove(70)
# print(s1)
print('\n')

#discard()
#if element not existed then it will not give any error
print('discard()')
print(s1)
print('s1.discard(70)')
s1.discard(70)
print(s1)
print('s1.discard(1000)')
s1.discard(1000)
print(s1)
print('s1.discard(20)')
s1.discard(20)
print(s1)
print('\n')

#pop()
#it will pop values
print('pop()')
print(s1)
v = s1.pop()
print('s1.pop()',v)
v = s1.pop()
print('s1.pop()',v)
v = s1.pop()
print('s1.pop()',v)
print(s1)
print('\n')

#intersection()
#it will return common values of two sets
print('Intersection()')
s1 = {0,1,2,3,4,5,6,7}
s2 = {1,3,5,7}
print('s1: ',s1)
print('s2: ',s2)
print('s1.intersection(s2) = ',s1.intersection(s2))
print('\n')

#union()
#it will return combined values of two sets
print('Union()')
s1 = {0,1,2,3,4,5,6,7}
s2 = {1,3,5,7}
print('s1: ',s1)
print('s2: ',s2)
print('s1.union(s2) = ',s1.union(s2))
print('\n')

#subset()
#it will check if one set is subset of other
print('issubset()')
s1 = {0,1,2,3,4,5,6,7}
s2 = {4,5,6,7}
print('s1: ',s1)
print('s2: ',s2)
print('s2.issubset(s1) = ',s2.issubset(s1))
print('\n')

#superset()
#it will check if one set is superset of other
print('issuperset()')
s1 = {0,1,2,3,4,5,6,7}
s2 = {4,5,6,7}
print('s1: ',s1)
print('s2: ',s2)
print('s1.issuperset(s2) = ',s1.issuperset(s2))
print('\n')