find=input("What are you looking for? ")
replace=input("Replace with what? ")
file_read=open("test.txt","r")
file_write=open("test2.txt","w")
for data in file_read:
	index=0
	while index<len(data):
		if data[index]==find[0]:
			if data[index:len(find)+index]==find:
				print(replace,end="",file=file_write)
				index+=len(find)-1
			else:
				print(data[index],end="",file=file_write)
		else:
			print(data[index],end="",file=file_write)
		index+=1
		