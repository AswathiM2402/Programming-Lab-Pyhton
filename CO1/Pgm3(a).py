#Programs using list comprehension
#Generate positive list of numbers from a given list of integers
list1=[4,7,8,,-2,-7,-8,-9,6]
i=[i for i in list1 if i>0]
print(i)