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
		return outputstring	


def thousands(num):
	numofthousands=(num-num%1000)/1000 #returns the number of 100's from number input
	if numofthousands>0:
		return units(numofthousands)+" Thousand"
	else:
		return ""

def hundreds(num):
	numofhundreds=(num%1000-num%100)/100 #returns the number of 100's from number input
	if numofhundreds>0:
		return units(numofhundreds)+" Hundred"
	else:
		return ""


def tens(num):
	numoftens=num%100-num%10 #Returns the number of 10's in number input
	if numoftens==20:
		return "Twenty"
	elif numoftens==30:
		return "Thirty"
	elif numoftens==40:
		return "Forty"
	elif numoftens==50:
		return "Fifty"
	elif numoftens==60:
		return "Sixty"
	elif numoftens==70:
		return "Seventy"
	elif numoftens==80:
		return "Eighty"
	elif numoftens==90:
		return "Ninety"
	else:
		return ""


def units(num):
	if num%10==1:
		return "One"
	elif num%10==2:
		return "Two"
	elif num%10==3:
		return "Three"
	elif num%10==4:
		return "Four"
	elif num%10==5:
		return "Five"
	elif num%10==6:
		return "Six"
	elif num%10==7:
		return "Seven"
	elif num%10==8:
		return "Eight"
	elif num%10==9:
		return "Nine"
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
			return "Zero"
		elif num==10:
			return "Ten"
		elif num==11:
			return "Eleven"
		elif num==12:
			return "Twelve"
		elif num==13:
			return "Thirteen"
		elif num==14:
			return "Fourteen"
		elif num==15:
			return "Fifteen"
		elif num==16:
			return "Sixteen"
		elif num==17:
			return "Seventeen"
		elif num==18:
			return "Eighteen"
		elif num==19:
			return "Nineteen"
	else:
		return ""


print(numtoword())