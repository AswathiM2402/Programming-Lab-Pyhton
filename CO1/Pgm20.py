list1=[1,2,3,4,5,6,7,8,9]
print("The list before removing even numbers:",list1)
for i in list1:
    if i%2==0:
        list1.remove(i)
print("The list after removing even numbers:",list1)