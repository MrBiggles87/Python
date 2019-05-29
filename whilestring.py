message=input("Give me a string: ")
i=0
while i<len(message): 
	asciicode=ord(message[i]) #stores asciicode as a variable
	print("The ASCII code of ", message[i], " is ",asciicode)
	i=i+1


