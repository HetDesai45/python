n = int(input("Enter number = "))

#  a)

# for row in range(1,n+1):
#   for col in range(1,row+1):
#     print(row,end='')
#   print()

# b)

for row in range(1,n+1):
  for col in range(row,0,-1):
    print(col,end='')
  print()
