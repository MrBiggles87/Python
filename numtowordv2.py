def numtoword():
	needinput=True
	while needinput:
		inputvalue=int(input("Please enter a number between 0 and 9999: "))
		needinput=not validation(inputvalue)
		if needinput:
			print("The number you entered was invalid, please enter a number between 0 and 9999: ")
		
	special=checkspecial(inputvalue)
	if len(special)>0:
		return special
	else:
		outputstring=""
		outputstring+=thousands(inputvalue)+" " if thousands(inputvalue) else ""
		outputstring+=hundreds(inputvalue)+" " if hundreds(inputvalue) else ""
		outputstring+="and " if tens(inputvalue) or units(inputvalue) else ""
		outputstring+=tens(inputvalue)+" " if tens(inputvalue) else ""
		outputstring+=units(inputvalue)
		outputstring=outputstring[0].upper()+outputstring[1:]
		return outputstring	


def thousands(num):
	numofthousands=(num-num%1000)/1000 #returns the number of 100's from number input
	if numofthousands>0:
		return units(numofthousands)+" thousand"
	else:
		return ""

def hundreds(num):
	numofhundreds=(num%1000-num%100)/100 #returns the number of 100's from number input
	if numofhundreds>0:
		return units(numofhundreds)+" hundred"
	else:
		return ""


def tens(num):
	numoftens=num%100-num%10 #Returns the number of 10's in number input
	if numoftens==20:
		return "twenty"
	elif numoftens==30:
		return "thirty"
	elif numoftens==40:
		return "forty"
	elif numoftens==50:
		return "fifty"
	elif numoftens==60:
		return "sixty"
	elif numoftens==70:
		return "seventy"
	elif numoftens==80:
		return "eighty"
	elif numoftens==90:
		return "ninety"
	else:
		return ""


def units(num):
	if num%10==1:
		return "one"
	elif num%10==2:
		return "two"
	elif num%10==3:
		return "three"
	elif num%10==4:
		return "four"
	elif num%10==5:
		return "five"
	elif num%10==6:
		return "six"
	elif num%10==7:
		return "seven"
	elif num%10==8:
		return "eight"
	elif num%10==9:
		return "nine"
	else:
		return ""


def validation(num):
	if num<0 or num>9999:
		return False
	else:
		return True


def checkspecial(num):
	if num==0 or (num>=10 and num<=19):
		if num==0:
			return "zero"
		elif num==10:
			return "ten"
		elif num==11:
			return "eleven"
		elif num==12:
			return "twelve"
		elif num==13:
			return "thirteen"
		elif num==14:
			return "fourteen"
		elif num==15:
			return "fifteen"
		elif num==16:
			return "sixteen"
		elif num==17:
			return "seventeen"
		elif num==18:
			return "eighteen"
		elif num==19:
			return "nineteen"
	else:
		return ""


print(numtoword())