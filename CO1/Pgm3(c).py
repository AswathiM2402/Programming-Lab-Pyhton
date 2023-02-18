#Programs using list comprehension
#Form a list of vowels selected from a given word
word=input("Enter a word:")
vowels=[i for i in word if i in "aeiouAEIOU"]
print("List of vowels in the given word",word,":",vowels)