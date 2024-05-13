import math

P=int(input("Enter Pricipal = "))
R=int(input("Enter rate of interest = "))
N=int(input("Enter time in year"))

def compunt_inerest(p,r,n):
  amount = p *(pow((1+r/100),n))
  ci = amount-p
  print("Compund Interest = ",ci)

compunt_inerest(P,R,N)