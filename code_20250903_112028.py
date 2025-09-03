def calculator(a: float, b: float) -> float:
    """
    Performs addition, subtraction, multiplication and division operations on two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Raises:
        TypeError: If the input type is not a float.
    """
    try:
        return a + b, a - b, a * b, a / b
    except TypeError as e:
        print(f"Error: {e}")