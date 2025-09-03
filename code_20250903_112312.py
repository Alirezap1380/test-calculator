def calculator(num1: float, num2: float) -> None:
    """
    Performs addition, subtraction, multiplication, and division operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Raises:
        TypeError: If either argument is not a float.
        ZeroDivisionError: If division by zero occurs.
    """
    operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}

    try:
        operation = input("Enter operation (+, -, *, /): ").strip()
        result = operations[operation]
        print(f"Result: {result}")
    except KeyError:
        print("Invalid operation. Please enter a valid operator (+, -, *, /)")
    except TypeError as e:
        print(str(e))