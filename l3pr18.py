n = int(input("Enter number = "))

string1 = input("Enter String1 = ")

length = len(string1)

if n>=length:
  print("Enter proper number")
else:
  final = string1[n:]
  print(final)