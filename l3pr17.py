string1 = input("Enter String = ")

strip = "aeiouAEIOU"

print("Original String : ",string1)
print("After stripping aeiou AEIOU :"," ".join(c for c in string1 if c not in strip))