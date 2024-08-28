import math

class Calculator:
    def __init__(self):
        # Constructor to initialize the calculator
        pass

    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract second number from the first."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide the first number by the second. Handle division by zero."""
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    def sqrt(self, x):
        """Compute the square root of a number. Handle negative input."""
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error: Cannot compute square root of a negative number"

    def perform_operation(self):
        """Display menu, take user input, and perform the selected operation."""
        while True:
            # Display the menu
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Square Root")
            print("6. Exit")

            # Get the user's choice of operation
            operation = input("Enter operation (1/2/3/4/5/6): ")

            # Exit the loop and end the program
            if operation == '6':
                print("Exiting...")
                break

            # Perform the operation based on user input
            if operation in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                if operation == '1':
                    print(f"{num1} + {num2} = {self.add(num1, num2)}")

                elif operation == '2':
                    print(f"{num1} - {num2} = {self.subtract(num1, num2)}")

                elif operation == '3':
                    print(f"{num1} * {num2} = {self.multiply(num1, num2)}")

                elif operation == '4':
                    result = self.divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

            elif operation == '5':
                try:
                    num = float(input("Enter number to find the square root: "))
                    result = self.sqrt(num)
                    print(f"Square root of {num} = {result}")

                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            else:
                print("Invalid input. Please choose a valid operation.")

# Create an instance of the Calculator class and perform operations
calc = Calculator()
calc.perform_operation()
