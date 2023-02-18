#Create a list of colors from comma-separated color names entered by user.Display first and last colors.
'''a=[]
for i in range(3):
    b=input("Enter the color:")
a.append(b)
print(a)
print(a[0])
print(a[-1])'''
color=input("Enter the list of colors seperated by ',':")
l1=color.split()
print("The list is:",l1)
print("First and last color is:",l1[0],l1[-1])