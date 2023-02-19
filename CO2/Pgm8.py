#Accept a list of words and return length of longest word
a=[]
n=int(input("Enter a number:"))
for i in range(0,n):
    e=input("Enter element:"+str(i+1))
    a.append(e)
    max=len(a[0])
    temp=a[0]
for x in a:
    if(len(x)>max):
        max=len(i)
        temp=i
print("Longest word:",temp)
print("Length of longest word:",max)