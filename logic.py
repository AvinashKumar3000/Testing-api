def add(x, y):
    # doing addition operation
    result = x + y
    return result

def subtract(x, y):
    # doing subtraction operation
    result = x - y
    return result

def multiply(x, y):
    # doing multiplication operation
    result = x * y
    return result

def divide(x, y):
    # doing division operation
    if y == 0:
        raise ValueError("Cannot divide by zero")
    result = x / y
    return result