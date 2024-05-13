import math

n=int(input("Enter n="))
r=int(input("Enter r="))

def ncr(n,r):
  valuencr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
  print(f"nCr = {valuencr}")


def npr(n,r):
  valuenpr = math.factorial(n)/math.factorial(n-r)
  print(f"nPr = {valuenpr}")

ncr(n,r)
npr(n,r)