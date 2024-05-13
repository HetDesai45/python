shape = input("Enter Shape = ")

def calculate(name):

  name = name.lower()
	
  if name == "rectangle":
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))

    area = l * b
    perimeter = 2*(l+b)
    print(f"The area of cylinder is {area}.")
    print(f"The perimeter of cylinder is {perimeter}.")

  elif name == "square":
    l = int(input("Enter lenght: "))
    
    # calculate area of square
    area = l*l
    perimeter=4*l
    print(f"The area of cylinder is {area}.")
    print(f"The perimeter of cylinder is {perimeter}.")

  elif name == "triangle":
    h = int(input("Enter height: "))
    b = int(input("Enter breadth: "))

    area = 0.5 * b * h
    print(f"The area of cylinder is {area}.")

  elif name == "circle":
    r = int(input("Enter radius: "))
  
    area = 3.14 * r * r
    perimeter=2*3.14*r
    print(f"The area of cicle is {area}.")
    print(f"The perimeter of circle is {perimeter}.")
      
  elif name == 'cylinder':
    r = int(input("Enter radius: "))
    h = int(input("Enter height: "))

    area = 2*3.14*r*h + 2*3.14*r*r
    perimeter = 4*r + 2*h
    print(f"The area of cylinder is {area}.")
    print(f"The perimeter of cylinder is {perimeter}.")
    
  else:
    print("Please enter valid input")

calculate(shape)