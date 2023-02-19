#Write lambda functions to find area of square,rectangle and triangle
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
h=int(input("Enter height: "))
ar=lambda x,y: x*y
asq=lambda x: x*x
at=lambda x,y:0.5*x*y
print("Area of rectangle:",ar(l,b))
print("Area of square:",asq(l))
print("Area of triangle:",at(l,b))


