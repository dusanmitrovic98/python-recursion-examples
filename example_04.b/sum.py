# Define function "sum", which returns the sum of all elements in a list of numbers 
# and all its sublists. It is forbidden to use loops and the sum function.

# Example: sum([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = 45

def sum(list):
    if not list:
        return 0
    elif isinstance(list[0], type(list)):
        return sum(list[0]) + sum(list[1:])
    else:
        return list[0] + sum(list[1:])

print(sum([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
