def change(message):
	index=0
	outputstring=""
	while index<len(message):
		asciicode=ord(message[index])
		if asciicode>=65 and asciicode<=90: #Checking to see if the character is an uppercase letter.
			asciicode=asciicode+32
		elif asciicode>=97 and asciicode<=122: #Checking to see if the character is lowercase.
			asciicode=asciicode-32
		elif asciicode>=48 and asciicode<=57: #Checking to see if the character is a number.
			asciicode=(asciicode-48)*(2)
			if asciicode>=10:
				outputstring=outputstring+chr(49)
				asciicode=asciicode-10
				asciicode=asciicode+48
			else:
				asciicode=asciicode+48

		outputstring=outputstring+chr(asciicode)

		index=index+1
	return outputstring

print(change(input("Enter ANY message: ")))

