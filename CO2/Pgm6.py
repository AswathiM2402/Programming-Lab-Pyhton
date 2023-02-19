#Count the number of characters in a string
a=str(input("Enter a string:"))
f={}
for i in a:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print("Number of all characters:"+str(f))