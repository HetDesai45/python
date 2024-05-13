name = input("Enter your name = ")
gender = input("Enter your gender M/F= ")

def addprefix(gen):
  if gen=='M':
    print("Mr.",name)
  else:
    print("Ms.",name)

addprefix(gender)