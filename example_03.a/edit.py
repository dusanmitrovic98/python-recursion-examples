# The function "edit", which increases each of the first n elements by a defined value and decreases the remaining elements by a defined value. 
# The function takes a list containing only numeric values and the value that needs to be increased or decreased as parameters. The use 
# of loops is forbidden.

# Example: edit([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]

def edit(list, count, step, result = [], counter = 0):
    if not list:
        return result
    if count > counter:
        result.append(list[0] + step)
    else:
        result.append(list[0] - step)
    return edit(list[1:], count, step, result, counter + 1)

print(edit([1, 2, 3, 4, 5], 3, 1))