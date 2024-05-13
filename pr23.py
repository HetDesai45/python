num = int(input("Enter Number = "))

def checkdivisible(number):
  if num%7 == 0:
    print(num,"is divisible by 7")
  else:
    print(num,"is not divisible by 7")

checkdivisible(num);