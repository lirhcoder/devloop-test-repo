"""Simple calculator module for DevLoop E2E testing."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    # Bug: no zero division check
    return a / b


def multiply(a: int, b: int) -> int:
    return a * b
