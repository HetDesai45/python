class library:
  def __init__(self):
    self.accno=0
    self.author=""
    self.title=""
    self.days=0
    self.charge=0
  
  def read(self):
    self.accno=int(input("Enter Account no ="))
    self.title=input("Enter Title of the book = ")
    self.author=input("Enter author of the book = ")
  
  def compute(self):
    self.days=int(input("Enter Number of Days for late submit = "))
    self.charge = self.days*15
  
  def display(self):
    print(f"ACC No = {self.accno}")
    print(f"Title = {self.title}")
    print(f"Author = {self.author}")
    print(f"No of days late = {self.days}")
    print(f"Total charge for late submission = {self.charge} rs.")

b1=library()
b1.read()
b1.compute()
b1.display()