import math

a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
c=int(input("Enter value of c="))

def qudratic():
  determine = b*b - 4*a*c
  val=math.sqrt(abs(determine))
  
  if determine>0:
    print("Real and different roots")
    print((-b + val)/(2*a))
    print((-b - val)/(2*a))
  elif determine==0:
    print("Real and same roots")
    print((-b)/(2*a))
  else:
    print("Complex roots")
    

qudratic()