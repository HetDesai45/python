num1 = int(input("Enter Number1 = "))
num2 = int(input("Enter Number2 = "))

def checkbig(n1,n2):
  if n1<n2:
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
    print("Number1 = ",n1)
    print("Number2 = ",n2)
  else:
    print("Number1 = ",n1)
    print("Number2 = ",n2)

checkbig(num1,num2)