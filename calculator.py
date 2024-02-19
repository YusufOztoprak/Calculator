
import math

def calculator():
    print(" 1. Add 2. Subtract \n 3. Multiply 4. Divide \n 5. Power 6. Modulus 7. Exit ")
    choice = int(input("Select operation: "))
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if choice == 1:
        print(x+y)
    elif choice == 2:
        print(x-y)
    elif choice == 3:
        print(x*y)
    elif choice == 4:
        print(x/y)
    elif choice == 5:
        print(x**y)
    elif choice == 6:
        print(x%y)
    elif choice == 7:
        print("Exiting...")
    else:
        print("Invalid Input")
        
        
calculator()




