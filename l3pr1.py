count = 100
sum=0

while count<200:
  if count%2==0:
    sum+=count

  count+=1

print(f"The sum of even digits between 100 and 200 = {sum}")