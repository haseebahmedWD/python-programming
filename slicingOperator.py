#it is used to extract some part of string and display it 
#write program to take input some words and display them in reverse word by word

s1 = '--'.join(input("Enter words: ").split(' ')[: : -1])
print(s1)