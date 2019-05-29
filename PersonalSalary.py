name=("Please Insert Your Name: ")
salary=int(input("Please Insert Your Salary: "))
tax1=int(salary)-(12500)*20/100
ni1=int(salary)-(12500)*12/100
net1=int(salary)-(tax1)-(ni1)
tax2=int(salary)-(12500)*20/100

print("Your Yearly Salary:",salary)
if salary<=12500:
	print("Salary: ",salary)
	print("National Insurance: ",salary-ni1)
	print("Tax: ",tax1)
	print(" ")
	print("Net Salary: ",net1)
if salary>12500:
	salary*20/100
	print("Salary: ",salary)
	print("National Insurance: ",salary-NI)
	print("Tax: ",salary-tax)
	print(" ")
	print("Net Salary: ",net)
if salary>50000: