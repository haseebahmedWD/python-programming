#creating a dict 
d1 = {101:'Ali',102:'Babar',103:'Muneeb',104:'Zain'}
print(d1)
print('\n')

#creating a dict using dict() method
#d2 = dict(102:'Kaleem',103:'Akmal',104:'Raheel')
d2 = dict(k='Kaleem',a='Akmal',r='Raheel')
print(d2)
print('\n')

#Accessing list elements
print("Printing dict")
print(d1)
#using index/keys
print(d1[101],d1[102],d1[103])
#for loop but it only print keys
for x in d1:
    print(x)
#for loop it print key-value
for x in d1:
    print(x,d1[x])

print('\n')

#Updating values in dict
print("Updating dict")
d1[103] = 'Mustafa' #updating previous value against key [103]
d1[106] = 'Saleem'  #creating new key [106] with value 'Saleem'
print(d1)
print('\n')

#dict methods
print("Printing dict key values seperate")
print('Keys: ',d1.keys())
print('Values: ',d1.values())
print('Key-Values: ',d1.items())
# for loop unpacking
for k,v in d1.items():
    print(k,v)
print('\n')

#Build-in methods in dict
print('Length: ',len(d1))
print('min: ',min(d1))
print('max: ',max(d1))
print('sum: ',sum(d1))
print('sorted: ',sorted(d1))
print('\n')

#Comparison in dict
print('dict comparison')
d2 = {101:'apple',102:'banana',103:'orange'}
d3 = {103:'orange',102:'banana',101:'apple'}
print('d2: ',d2)
print('d3: ',d3)
print("d2 == d3: ",d2 == d3)
print('\n')

#Dict comprehension
print('dict comprehension')
d4 = {a:a**2 for a in range(1,8,1)}
print(d4)
print('\n')
