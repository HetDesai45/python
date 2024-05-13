principal = int(input("Enter the principal/money lent = "));
rate = int(input("Enter rate of interest = "));
time = int(input("Enter time = "));

si = (principal*rate*time)/100;
apayable=principal+si;

print("Simple interest = ",si);
print("Amount payable = ",apayable);
