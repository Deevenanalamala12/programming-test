class Calculator:
    def __init__(self):
        pass
    
    def calculate(self, a, b, operation):
        operation = operation.lower()
        
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                return "Error: Division by zero is not allowed"
            return a / b
        else:
            return "Error: Invalid operation"

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.calculate(10, 5, "add"))
    print("Subtraction:", calc.calculate(10, 5, "subtract"))
    print("Multiplication:", calc.calculate(10, 5, "multiply"))
    print("Division:", calc.calculate(10, 5, "divide"))
