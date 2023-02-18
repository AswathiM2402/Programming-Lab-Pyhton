n=int(input("Enter the number of elements:"))
list1=[]
for i in range(n):
    num=int(input("Enter the elements:"))
    if num>=100:
        list1.append('over')
    else:
        list1.append(num)
    print(list1)