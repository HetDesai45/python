class Employee:
  def setdata(self):
    name=[]
    eid=[]
    salary=[]
    n = int(input("Enter how many employee detail you want to store = "))
    for i in range(0,n):
      ename = input("Enter Employee Name = ")
      empid = int(input("Enter Employee ID = "))
      esalary = int(input("Enter Employee Salary = "))
      name.append(ename)
      eid.append(empid)
      salary.append(esalary)
      print("----------------------")

    print("------Employee Details------")
    for i in range (0,n):
      print(f"Name = {name[i]}")
      print(f"ID = {eid[i]}")
      print(f"Salary = {salary[i]}")
      print("----------------------")

employee1 = Employee()

employee1.setdata()
