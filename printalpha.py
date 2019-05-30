alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
message=input("Enter any message: ")

i=0
while i<len(message):
	if not ord(message[i])==32:
		alpha[ord(message[i].upper())-65]+=1
	i+=1


i=0
while i<=25:
	if alpha[i]>0:
		print(chr(i+65),"=",alpha[i])
	i+=1