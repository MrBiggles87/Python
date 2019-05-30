# Python code to remove duplicate elements 
def Remove(duplicate): 
    numlist = [] 
    for num in duplicate: 
        if num not in numlist: 
            numlist.append(num) 
    return numlist
      
# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) 