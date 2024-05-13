file1 = open("myfile.txt", "w")
 
file1.write("Hello \n")
file1.write("How are you? \n")
file1.write("where are you from? \n")
file1.write("what is your fav food? \n")
file1.close() 
 
file1 = open("myfile.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())

file1.close()