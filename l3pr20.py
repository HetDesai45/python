# a)

# date = input("Enter date in dd/mm/yyyy format = ")

# date1 = date.replace("/","-")

# print(date1)

# b)

string = input("Enter String = ")
character = input("Enter character = ")

count = len(string.split(character)) - 1
print(count)