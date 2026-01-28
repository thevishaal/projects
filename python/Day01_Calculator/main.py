def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "**":
        return num1 ** num2
    else:
       raise ValueError

while True:
    choice = input("Exit the Calculator press (q) and continue (c): ").lower().strip()

    if choice == "q":
        print("Calculator closed!")
        break
    elif choice != "c":
        print("Please choose 'c' to continue and 'q' to quit.")
        continue

    try:
        operator = input("Select operator(+, -, *, /, %, **): ").strip()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = calculator(operator, num1, num2)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input or operator!")