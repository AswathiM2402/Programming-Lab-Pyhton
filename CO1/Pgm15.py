list1=set(["pink","blue","red","white"])
list2=set(["violet","pink","red"])
print("The first list is:",list1)
print("The second list is:",list2)
print("Colors contained in first list that are not contained in second list are:")
print(list1.difference(list2))