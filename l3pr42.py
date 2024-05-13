set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

if set1.isdisjoint(set2):
  print("No common items")
else:
  print(set1.intersection(set2))