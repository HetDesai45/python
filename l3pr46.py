dict1={'het' : 7410852963, 'om' : 9638520741}

name=input("Enter Name = ")
phoneno = input("Enter Phone No =")

if name not in dict1.keys():
  dict1[name] = phoneno
else:
  print("Name is already present in dict")

print(dict1)