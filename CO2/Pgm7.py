#Add 'ing' at the end of a given string.If it already ends with 'ing',then add 'ly'
string = input("enter a string:")
if string.endswith('ing'):
    string += 'ly'
elif len(string) >= 1:
         string += 'ing'
print(string)