# Basic Calculator Program

def calculator():
    print("Basic Calculator")
    print("Operations available: + (addition), - (subtraction), * (multiplication), / (division)")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation! Please use one of: +, -, *, /")
            return
        
        # Display the result
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the calculator
calculator()