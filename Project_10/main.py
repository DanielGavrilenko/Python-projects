from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

while True:
    num1 = float(input("Enter the first number: "))
    for operation_symbol in operations:
        print(operation_symbol)
    operation = input("Pick an operation: ")
    num2 = float(input("Enter the second number: "))

    if operation in operations:
        result = operations[operation](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation!")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        break
