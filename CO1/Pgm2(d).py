#To list ordinal values of each element of a word
word=input("Enter a word:")
n=[ord(i) for i in word]
print("Ordinal values of each element in the word",word,"are:",n)
