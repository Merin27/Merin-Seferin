class Calculator:
    def calculate(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (add/sub/mul/div): ")

        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            return a / b if b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

calc = Calculator()
print("Result:", calc.calculate())
