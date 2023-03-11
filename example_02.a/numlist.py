# define function "numlist", which extracts only numerical values from a list that can contain elements of different types.
# Example: numlist(["First", "Second", 2, 4, [3, 5]]) = [2, 4]

def numlist(list):
    if not list:
        return []
    elif isinstance(list[0], int) or isinstance(list[0], float):
        return [list[0]] + numlist(list[1:])
    # elif isinstance(list[0], list): # This will add sub numeric lists as well
    #     return numlist(list[0]) + numlist(list[1:])
    else:
        return numlist(list[1:])

# print(numlist(["First", "Second", 2, 4, [3, 5]])) # expected output: [2, 4]