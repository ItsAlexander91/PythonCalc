from operations.basic import add, subtract, multiply, divide
from operations.scientific import sin, cos, tan, log
from operations.conversions import convert_units
from settings.config import settings

def main():
    print("Welcome to the Ultimate Python Calculator!")
    print("Choose an option:")
    print("1. Basic Operations")
    print("2. Scientific Calculations")
    print("3. Unit Conversions")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Example: Basic operation
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print("Choose operation: +, -, *, /")
        op = input("Enter operation: ")
        
        if op == '+':
            print("Result:", add(x, y))
        elif op == '-':
            print("Result:", subtract(x, y))
        elif op == '*':
            print("Result:", multiply(x, y))
        elif op == '/':
            print("Result:", divide(x, y))
        else:
            print("Invalid operation.")

    elif choice == '2':
        # Example: Scientific operation
        angle = float(input("Enter an angle in degrees: "))
        print("sin:", sin(angle))
        print("cos:", cos(angle))
        print("tan:", tan(angle))

    elif choice == '3':
        # Example: Unit conversion
        value = float(input("Enter value: "))
        print("1. Meters to Kilometers")
        print("2. Celsius to Fahrenheit")
        print("3. Grams to Kilograms")
        unit_choice = input("Enter your choice: ")
        result = convert_units(value, unit_choice)
        print("Converted value:", result)

    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
