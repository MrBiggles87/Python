numbers=[]
while True:
	num=int(input("Enter any number (Press 0 to exit): "))
	if num==0:
		break
	else:
		numbers.append(num)


highest=numbers[0]
index=1
elements=len(numbers)
while index<elements:
	if numbers[index]>highest:
		highest=numbers[index]
	index=index+1
print(" ")
print("Highest Number: ",highest)