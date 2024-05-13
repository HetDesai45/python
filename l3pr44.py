import numpy as np

dict = {'a': 97, 'e': 101,'c': 99, 'd': 100}
print(dict)

list1 =[]

for i in dict.values():
  list1.append(i)

list1.sort()


print(f"Highest value is = {list1[-1]}")
print(f"Second Highest value is = {list1[-2]}")