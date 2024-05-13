num = int(input("Enter Number = "));
sum=0;
for i in range(1,num+1):
  sum=float(sum+(1/(i*i*i)));

print("Sum = ",sum);