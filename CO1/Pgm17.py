#sort dictionary in ascending and descending order.
dict={"Alice":18,"Bob":36,"Surya":22}
s=sorted(dict.items())
print("In ascending order:",s)
s1=sorted(dict.items(),reverse=True)
print("In descending order:",s1)