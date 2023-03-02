string = input()
result = []
for word in string.split(" "):
  result.append(word.capitalize())

str = " ".join(result)
print(str)
  

