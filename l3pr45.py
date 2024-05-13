st = input("Enter a string: ")

dic = {}
#creates an empty dictionary

for ch in st:
  if ch in dic:
    dic[ch] += 1
  else:
    dic[ch] = 1

print(dic)