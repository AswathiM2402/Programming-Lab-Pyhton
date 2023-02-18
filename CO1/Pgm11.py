#Find biggest of 3 numbers
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if x>y:
    if x>z:
        print("The first number",x,"is largest")
elif y>z:
    print("The second number",y,"is largest")
else:
   print("The third number",z,"is largest")
