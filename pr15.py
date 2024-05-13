min = 0;
max = 0;

for i in range(0,5):
  num=int(input("Enter number = "));
  if(i == 0):
    min=max=num;
  if(num < min):
    min=num;
  if(num>max):
    max=num;

print("Minimum number is = ",min);
print("Maximum number is = ",max)