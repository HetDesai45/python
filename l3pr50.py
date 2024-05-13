class Student:
  def __init__(self):
    self.name=[]
    self.marks=[]
  
  def setdata(self):
    for _ in range(5):
      n = input("Enter student Name = ")
      m = input("Enter Marks = ")
      self.name.append(n)
      self.marks.append(m)
      print("------------------")

class Marks(Student):
  def getdata(self):
    print("Student Details -----")
    print("*****************************")
    for i in range(5):
      print(f"Name of student = {self.name[i]}")
      print(f"Marks = {self.marks[i]}")
      print("------------------")


s1=Marks()

s1.setdata()
s1.getdata()