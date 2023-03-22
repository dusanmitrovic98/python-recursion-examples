# Define function "operation", which that transforms a list of tuples into a list of numbers obtained by applying the operation passed as an argument.
# Example: operation([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y) = [11, 6, 5].

def operation(A, op):
    if not A:
        return []
    if not isinstance(A, list):
        if len(A) == 1:
            return A[0]
        elif len(A) == 2:
            return op(A[0], A[1])
        elif len(A) > 2:
            return op(A[0], operation(A[1:], op))
    else:
        return [operation(A[0], op)] + operation(A[1:], op)


print(operation([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y))
