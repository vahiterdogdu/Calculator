def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))
print(add(5, 3))
print(subtract(10, 77))

