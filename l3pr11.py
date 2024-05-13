n1=int(input("Enter Number1="))
n2=int(input("Enter Number2="))

def arithmetic(num1,num2):
  sum=num1+num2
  sub=num1-num2
  mul=num1*num2
  div=num1/num2

  print(f"Addition = {sum}")
  print(f"Subtraction = {sub}")
  print(f"Multiplication = {mul}")
  print(f"Division = {div}")


arithmetic(n1,n2)