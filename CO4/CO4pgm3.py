class Rectangle:
    def __init__(self):
        self.__l = int(input("Enter the length: "))
        self.__b = int(input("Enter the breadth: "))
    def __lt__(self,ob2):
        area1=self.__l*self.__b
        area2=ob2.__l*ob2.__b
        print("Area of rectangle 1 is: ",area1)
        print("Area of rectangle 2 is: ",area2)
        return area1<area2
print("Enter the length and breadth of first rectangle: ")
ob1=Rectangle()
print("Enter the length and breadth of second rectangle: ")
ob2=Rectangle()
if ob1<ob2:
    print("Rectangle1 is less than Rectangle2")
else:
    print("Rectangle1 is greater than Rectangle2")
    '''def get_perimeter(self):
        return 2 * (self.l + self.b)
    
    def get_area(self):
        return self.l * self.b
    
    def compare(self,obj2):
        if obj1.get_area() == obj2.get_area():
            print("Area of both rectangles are the same")
        elif obj1.get_area() > obj2.get_area():
            print("Area of Rectangle 1 is greater")
        else:
            print("Area of Rectangle 2 is greater")

obj1=Rectangle()
obj2=Rectangle()
print("Area of rectangle: ",(obj1.get_area()))
print("Perimeter of rectangle: ",(obj1.get_perimeter()))
print("Area of rectangle: ",(obj2.get_area()))
print("Perimeter of rectangle: ",(obj2.get_perimeter()))
print("Perimeter of rectangle: ",(obj2.get_perimeter()))
obj1.compare(obj2)'''

