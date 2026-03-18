def cal():

    print('''Choice 1: Area of square 
    Choice 2: Area of rectangular 
    Choice 3: Area of circle
    Choice 4: Area of triangle''')

    Choice = int(input("Enter your choice: "))

    if Choice == 1:
        print("Area of square")
        Side = float(input("Enter the side of square: "))
        Area = Side**2
        print("The area of square:", Area)

    elif Choice == 2:
        print("Area of rectangular")
        Length = float(input("Enter the length of rectangular: "))
        Width = float(input("Enter the width of rectangular: "))
        Area = Length * Width
        print("The area of rectangular:", Area)

    elif Choice == 4:
        print("Area of triangle")
        Length = float(input("Enter the length of triangle: "))
        Width = float(input("Enter the width of triangle: "))
        Area = Length * Width/2
        print("The area of Triangle:", Area)

    elif Choice == 3:
        print("Area of circle")
        Radius = float(input("Enter the radius of circle: "))
        Area = 3.14 * Radius**2
        print("The area of Circle:", Area)

    else:
        print("Enter the valid Choice.")

cal()