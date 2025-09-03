def calculator(a: float, b: float) -> float:
    """Performs addition, subtraction, multiplication, and division operations on two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Raises:
        TypeError: If either argument is not a float.
        ZeroDivisionError: If dividing by zero.

    Returns:
        float: Result of the calculation.
    """
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b if b != 0 else None

        return {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division
        }
    except TypeError as e:
        raise ValueError(f"Both arguments must be numbers. Got type error: {e}")