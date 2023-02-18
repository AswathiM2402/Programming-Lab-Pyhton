#Create a string separated with space from 2 strings by swapping the character at position l.
str1=input("Enter the first string:")
str2=input("Enter the second string:")
s1=str1[0]
s2=str2[0]
print("Output:",s2+str1[1:],"and",s1+str2[1:])