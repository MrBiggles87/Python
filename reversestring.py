message=input("Input a word to reverse: ")

for char in range(len(message) - 1, -1, -1):
  print(message[char], end="")
print("\n")