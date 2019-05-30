def removeduplicate(lists):
   index=0
   while index<len(lists):
      j=index+1
      while j<len(lists):
         if lists[index]==lists[j]:
            del lists[j]
         else:
            j+=1
      index+=1

s=['cat','dog','cat','mouse','dog','dog',]
removeduplicate(s)
print(s)