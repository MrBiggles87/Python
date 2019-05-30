try:
	no1=(int(input("Please Enter First Number: ")))
	no2=(int(input("Please Enter Second Number: ")))
	result=no1/no2
	print("Result = ",result)
except ValueError:
	print(" ")
	print("Please Enter ONLY Digits, Try Again...")
except ZeroDivisionError:
	print(" ")
	print("Cannot Divide By Zero! Try Again...")