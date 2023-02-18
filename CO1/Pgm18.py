#Merge two dictionaries
d1={"Name:":"Aswathi","Age":"21"}
d2={"dob":"27/02/2001"}
d=d1.copy()
d.update(d2)
print(d)