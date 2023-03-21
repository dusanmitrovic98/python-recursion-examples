# Define function "merge", which is a function that merges two lists of numbers into a single list consisting of number pairs (tuples).
# The length of the list should be greater than two input lists. The n-th tuple data of the resulting collection
# consists of the n-th numbers from both input lists, where the smaller number should be in the first position,
# and the larger number in the second position. The shorter input list should be padded with zeros at the end
# until the lengths of both lists are equal. The use of loops is forbidden (except in comprehension syntax).
# Example: merge([1, 7, 2, 4, 5], [2, 5, 2]) = [(1, 2), (5, 7), (2, 2), (0, 4), (0, 5)].

def merge(listA, listB):
    if not listA and not listB:
        return []
    else:
        elementA = listA[0] if listA else 0
        elementB = listB[0] if listB else 0
        temp_result = None
        if elementA < elementB:
            temp_result = (elementA, elementB)
        else:
            temp_result = (elementB, elementA)
        return [temp_result] + merge(listA[1:], listB[1:])


print(merge([1, 7, 2, 4, 5], [2, 5, 2]))
