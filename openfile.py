file_read=open("test.txt","r")
file_write=open("test2.txt","w")
for data in file_read:
	print(data,file=file_write)