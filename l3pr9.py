import math

n=int(input("Enter Number = "))

# a
# sum=0
# for i in range(1,n+1):
#   sum+=1/i

# print(sum)

# b)

sum=0

for i in range(1,n+1):
  sum+=pow(i,i)/i

print(sum)
