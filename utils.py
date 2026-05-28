"""
Exemplary calculator functions
"""


def add(a: int, b: int) -> int:
    """Adds two numbers a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts number b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiplies two numbers a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divides number a by b."""
    return a / b


def decimal_to_binary(n: int) -> str:
    """Converts a decimal number to binary string."""
    if n < 0 or n > 100:
        raise ValueError("Liczba musi być z zakresu od 0 do 100")
    if not isinstance(n, int):
        raise ValueError("Liczba musi być naturalna")
    return bin(n)[2:]
