# Define function "join", which combines 2 lists of numbers into one list consisting of tuple objects that have three elements. 
# The first element of the resulting collection is an element of the first list, the second is an element of the 
# second list, and the third is the sum of the elements. The length of the list is the dimension longer than the 
# two input lists. The n-th tuple data of the resulting collection are the n-th numbers from both input lists, 
# where the smaller number should be at the first position and the larger number at the second position.

# The shorter input list should be padded with the number 0 at the end until the lengths of both lists are equal. Using loops is prohibited.

# Example: join([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 3), (5, 7, 12), (2, 2, 4), (4, 0, 4)]

def join(list1, list2, result = []):
    if not list1 and not list2:
        return result
    a = list1[0] if list1 else 0
    b = list2[0] if list2 else 0
    result.append((a, b, a + b))
    return join(list1[1:], list2[1:], result)

print(join([1, 7, 2, 4], [2, 5, 2]))