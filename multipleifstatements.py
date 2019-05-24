num=int(input("Please enter ANY number:."))
if num>1000:
	print("B")
	if num>2000:
		print("C")
	else:
		print("F")
	print("2")
else:
	if num<1000:
		print("A")
		if num>500:
			print("D")
		else:
			print("E")
		print("1")
print("3")
