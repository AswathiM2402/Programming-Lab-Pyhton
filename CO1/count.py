#Count the occurences of each word in a line of text.
str1=input("Enter a string:")
word=str1.split()
count=[]
for w in word:
    count.append(word.count(w))
print("Number of occurences:"+str(list(zip(word,count))))

def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count('apple apple mango'))