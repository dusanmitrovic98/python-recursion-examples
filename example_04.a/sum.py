# Define function "sum", which creates a new list whose elements are the sums of adjacent
# elements of the original list. Example: sum([1, 2, 3, 4, 5]) = [3, 5, 7, 9]

def sum(list):
    if len(list) < 2:
        return []
    return [list[0] + list[1]] + sum(list[1:])

print(sum([1, 2, 3, 4, 5]))