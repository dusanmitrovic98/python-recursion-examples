# Aditional simple collection of python recursion examples

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
