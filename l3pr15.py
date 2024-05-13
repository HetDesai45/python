def midstring():

  string1 = input("Enter String = ")

  mid = input("Enter Middle String = ")

  
  print("The original string is " + str(string1))
  temp = string1.split()
  mid_pos = len(temp) // 2

  res = temp[:mid_pos] + [mid] + temp[mid_pos:]

  res = ' '.join(res)

  print(mid_pos)

  print("String = " + str(res))


midstring();