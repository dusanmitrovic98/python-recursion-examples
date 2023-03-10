# Define function 'even', which determines the number of even elements in the given list.
# Example: even([1, 7, 2, 4, 5]) = 2.

def even(list):
    if not list:
        return 0
    if (list[0] % 2 == 0):
        return 1 + even(list[1:])
    else: 
        return 0 + even(list[1:])

print(even([1, 7, 2, 4, 5]))