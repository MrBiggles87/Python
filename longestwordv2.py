message=input("Please input any sentence: ")
message+=" "
current_word=""
longest_word=""
for ch in message:
	if ch==" ":
		if len(current_word)>len(longest_word):
			longest_word=current_word
			current_word=""
		else:
			current_word=""
	else:
		current_word+=ch
print(longest_word)