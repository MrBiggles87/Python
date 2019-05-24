Amount=input("Please Enter Amount for Withdraw :")

print "\n\nRequired notes of 100 is : " , Amount / 100
print "Required notes of 50 is : " , (Amount % 100) / 50
print "Required notes of 10 is : " , (((Amount % 100) % 50) / 10)
print "Amount still remaining is : " , (((Amount % 100) % 50) % 10)