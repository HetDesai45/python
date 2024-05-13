n = int(input("Enter Lines To Read = "))
f = open("myfile.txt","r")
for i in range(n):
	print(f.readline())