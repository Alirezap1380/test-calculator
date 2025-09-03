def fibonacci(n: int = 10) -> list:
    try:
        sequence = [0, 1]
        if n <= 0:
            raise ValueError("Number of elements in the sequence must be greater than 0")
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    except ValueError as e:
        print(f"Error: {e}")
        return []