#Program to find factorial of a number
fact=1
n=int(input("Enter a number:"))
if n==0:
    print("Factorial=",0)
else:
    while n>1:
        fact=fact*n
        n=n-1
    print(fact)