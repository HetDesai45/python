num=int(input("Enter Number = "));
rem=0;
add=0;
while num!=0:
  rem=num%10;
  add=add+rem;
  num=num//10;

print("The sum of digits of an integer number = ",add);