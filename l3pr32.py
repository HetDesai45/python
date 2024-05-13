import math

def findgdc(num1,num2):
  print(f"The gcd of {num1} and {num2} is = ", end="")
  print(math.gcd(num1,num2))

n1=int(input("Enter Number1 = "))
n2=int(input("Enter Number2 = "))
findgdc(n1,n2)