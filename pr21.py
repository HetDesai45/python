# i)*
#   * * *
#   * * * * *
#   * * *
#   *

n = int(input("Enter Number = "));

# for row in range(1,2*n):
#   if row > n :
#     totalcol = 2*n - row;
#   else: 
#     totalcol = row;
  
#   if totalcol%2 == 0:
#     continue

#   for col in range(0,totalcol):
#     print("*", end=' ')
  
#   print("\r")

  
# ii) 1
#     2 1 2
#     3 2 1 2 3
#     4 3 2 1 2 3 4
#     5 4 3 2 1 2 3 4 5

# for row in range(1,n):
#   if row>1:
#     totalcol=row+1
#   else:
#     totalcol=row
#   for col in range(row,0,-1):
#     print(col, end=' '  
#   for i in range(totalcol-1,1,-1):
#     print(totalcol-i+1, end=' ')
#   print("\r")

# iii)1 2 3 4 5
#     1 2 3 4
#     1 2 3
#     1 2
#     1

# for row in range(n,0,-1):
#   for col in range(1,row+1):
#     print(col, end=' ')

#   print("\r")

# iv) *
#     * *
#     * *
#     * *
#     *
  
for row in range(1,n+1):
  for col in range(1,row+1):
    if row==n:
      print("* ",end=' ')
      break
    elif row>1:
      print("* * ",end=' ')
      break
    else:
      print("* ",end=' ')
      break
  print("\r")
  
