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
    if not isinstance(n, int) or n < 0:
        raise ValueError("Liczba musi być naturalna")
    if n > 100:
        raise ValueError("Liczba musi być z zakresu od 0 do 100")
    return bin(n)[2:]
