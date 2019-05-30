def reversewords(Sentence): 
    return ' '.join(word[::-1] for word in Sentence.split(" "))   
Sentence=input("Please enter a message: ")
print(reversewords(Sentence))