x = int(input("Enter no of working days os A = "))
y = int(input("Enter no of working days os B = "))
z = int(input("Enter no of working days os C = "))

totalwork=(x*y*z)/((x*y)+(y*z)+(x*z));

print("They work together is ",totalwork,"days");
