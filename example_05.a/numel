# Define function "numel" counts the number of elements in each sub-list of a list that is passed to it. 
# If an element of the list is not a sub-list, the function returns -1.

# Example: numel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]

def numel(list):
    if not list:
        return []
    elif isinstance(list[0], type(list)):
        return [len(list[0])] + numel(list[1:])
    else:
        return [-1] + numel(list[1:])
    
print(numel([[1, 2], [3, 4, 5], 'el', ['1', 1]]))