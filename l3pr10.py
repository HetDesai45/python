word=str(input("Enter String = "))

vowel=["a","e","i","o","u","A","E","I","O","U"]
result=""

for i in range(len(word)):
  if word[i] not in vowel:
    result+=word[i]

print(f"String without vowel is = {result}")

