import math

class quadratic:
  def __init__(self):
    self.a=int(input("Enter value of a="))
    self.b=int(input("Enter value of b="))
    self.c=int(input("Enter value of c="))

  def roots(self):
    determine = self.b*self.b - 4*self.a*self.c
    val=math.sqrt(abs(determine))
    
    if determine>0:
      print("Real and different roots")
      print((-self.b + val)/(2*self.a))
      print((-self.b - val)/(2*self.a))
    elif determine==0:
      print("Real and same roots")
      print   ((-self.b)/(2*self.a))
    else:
      print("Complex roots")

r1=quadratic()
r1.roots()