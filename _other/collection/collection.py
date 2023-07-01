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
        return base * power(base, exponent - 1)

def binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binary_search(arr[mid + 1:], target)
        else:
            return binary_search(arr[:mid], target)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
