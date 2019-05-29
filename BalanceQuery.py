item=int(input("Please Enter Price of Item: "))
total=int(input("Please Enter Amount Given: "))
balance=total-item
print(" ")
print("Amount owed:",balance)
print(" ")
fifty=int(balance/50)
if fifty>0:
	print("£50: ",fifty)
	balance=balance%50
twenty=int(balance/20)
if twenty>0:
	print("£20: ",twenty)
	balance=balance%20
ten=int(balance/10)
if ten>0:
	print("£10: ",ten)
	balance=balance%10
five=int(balance/5)
if five>0:
	print("£5: ",five)
	balance=balance%5
one=int(balance/1)
if one>0:
	print("£1: ",one)
	balance=balance%1
fiftyp=float(balance/0.50)
if fiftyp<0:
	print("50p: ",fiftyp)
	balance=balance%0.5
print(" ")
print("Transaction Completed")
