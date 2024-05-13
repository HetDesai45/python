num1=int(input("Enter Number1="))
num2=int(input("Enter Number2="))
num3=int(input("Enter Number3="))


def biggest(n1,n2,n3):

  if n1>n2 and n1>n3:
    print(f"{n1} is largest")
  elif n2>n1 and n2>n3:
    print(f"{n2} is largest")
  elif n3>n1 and n3>n2:
    print(f"{n3} is largest")
  elif n1==n2 and n1>n3:
    print(f"{n1} and {n2} are equal and largest")
  elif n2==n3 and n2>n1:
    print(f"{n2} and {n3} are equal and largest")
  elif n1==n3 and n1>n2:
    print(f"{n1} and {n3} are equal and largest")
  else:
    print(f"{n1}, {n2} and {n3} are equal and largest")

biggest(num1,num2,num3)