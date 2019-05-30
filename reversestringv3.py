def reverse(word):
	newword=""
	index=len(word)-1
	while index>=0:
		newword=newword+word[index]
		index-=1
	return newword


message=input("Enter Any Message: ")
newmessage=""
word=""
for ch in message:
	if ch==" ":
		newmessage+=(reverse(word)+" ")
		word=""
	else:
		word+=ch
newmessage+=(reverse(word)+" ")
print(newmessage)