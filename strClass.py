e_str = str() #empty string
l_str = str([1,2,3,4,5])
print(l_str)
#print(sum(l_str))
print('\n')

#string indexing
s1 = "Mysirg Education Service"
print(s1)
print('"e" is at index: ',s1.index('e'))
print('"E" is at index: ',s1.index('E'))
print('"ice" is at index: ',s1.index('ice')) #it will get the starting index
print('\n')

#Built in methods
print(s1)
print('Length: ',len(s1))
print('Min: ',min(s1))
print('Max: ',max(s1))
print('Sorted: ',sorted(s1))
print('\n')

#comparison operator
s1 = '''Lahore'''
s2 = '''Islamabad'''
if s1>s2:
    print(s1, ' > ' ,s2)
else:
    print(s1, ' < ' ,s2)
print('\n')

#count()
s1 = "Mysirg Education Service"
print(s1)
print("'e' come in string ",s1.count('e'), 'times')
print("'blank space' come in string ",s1.count(' '), 'times')
print('\n')

#startswith()
s1 = "Mysirg Education Service"
print(s1)
print('string start with "My":',s1.startswith('My'))
print('\n')

#endswith()
s1 = "Mysirg Education Service"
print(s1)
print('string ends with "Ser":',s1.endswith('Ser'))
print('\n')

#isdigit()
s1 = "a123"
print(s1)
print('string is digit:',s1.isdigit())
s1 = "1234567"
print(s1)
print('string is digit:',s1.isdigit())
print('\n')

#isupper(), islower(), upper()
s1 = "Mysirg Education Service"
print(s1)
print('string is upper case:',s1.isupper())
print('string is lower case:',s1.islower())
print('\n')
s2 = 'HELLO WORLD'
s3 = 'hello world'
print(s2)
print('string is upper case:',s2.isupper())
print(s3)
print('string is lower case:',s3.islower())
print('in upper case:',s3.upper())
print('\n')

#replace()
s1 = "Mysirg Education Service"
print(s1)
print('replacing m with M: ',s1.replace('m','M'))
print('replacing all i with I: ',s1.replace('i','I',s1.count('i')))
print('\n')

#format()
s1 = "sum of {} and {} = {}"
print(s1)
print(s1.format(2,10,2+10))
#another way to write this with indexes
s2 = "{0} * {1} = {2}"
print(s2)
a = 2
b = 6
print(s2.format(a,b,a*b))
print('\n')

#split a string and join it
s1 = 'Mysirg Education Services'
print(s1)
s1 = s1.split(' ')
print("After split: ",s1,'\n')
strobj = ' '
print("Join with space: ", strobj.join(s1),'\n')
strobj = '-'
print("Join with '-': ", strobj.join(s1),'\n')

print("Join with '/': ", '/'.join(s1),'\n')

#Exp: Take input with whitespace seperate integers, split them, sum them!
s1 = (input("Enter numbers with space seperation: "))
print(s1)
#spliting
s1 = s1.split(' ')
print("After spliting:",s1)


# #put them in list
# s1 = [int(x) for x in s1]
# print(s1)

#sum
sum = 0
for x in s1:
    sum = sum + int(x)
print('Sum is: ',sum)