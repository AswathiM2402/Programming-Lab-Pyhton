def gcd(a,b):
    if(b==0):
        return a
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
if gcd(a,b):
    print("gcd of",a,"and",b,"is:",gcd(a,b))
else:
    print("Not found")