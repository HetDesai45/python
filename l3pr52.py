class clock:
  def settime(self):
    self.hour=input("Enter Hour = ")
    self.min=input("Enter Minute = ")
    self.second=input("Enter Seconds = ")
    

class calender:
  def setdate(self):
    self.day=input("Enter Day = ")
    self.month=input("Enter Month = ")
    self.year=input("Enter Year = ")


class calenderclock(clock,calender):
  def display(self):
    print(f"Date : {self.day}/{self.month}/{self.year}  {self.hour}:{self.min}:{self.second}")


c1=calenderclock()
c1.settime()
c1.setdate()
c1.display()

