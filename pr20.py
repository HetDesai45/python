num=int(input("Enter Number = "));
rem=0;
rev=0;
temp=num;
while temp!=0:
  rem=temp%10;
  rev=(rev*10)+rem;
  temp=temp//10;

if(num==rev):
  print("Given number is palindeome");
else:
  print("Given number is not palindrome number");