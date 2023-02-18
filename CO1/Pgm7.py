list1=[1,3,4,5,6,7]
list2=[4,5,2,9,3]
list3=[]
if len(list1)==len(list2):
    print("Length of both lists are same.")
else:
    print("Length of lists are not same.")
sum1=0
for i in list1:
    sum1=sum1+i
sum2=0
for i in list2:
    sum2=sum2+i
if sum1==sum2:
    print("Sum of lists are same.")
else:
    print("Sum of lists are not same")
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print("Common elements are:",list3)