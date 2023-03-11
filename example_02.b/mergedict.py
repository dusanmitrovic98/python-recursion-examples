# define function "mergedict", which merges two lists of objects into a list with elements of type dictionary. The length of the resulting list is equal to the length 
# of the longer of the two input lists. The n-th dictionary element of the resulting collection consists of the n-th objects from both input lists, 
# where the first position contains the element from the first list paired with the key 'first', and the second position contains the element from the 
# second list paired with the key 'second'. The shorter input list should be padded with ' - ' until both lists have the same length. Loops are forbidden.
# Example: mergedict([1, 7, 2, 4], [2, 5, 2]) = [{'first': 1, 'second': 2}, {'first': 7, 'second': 5}, {'first': 2, 'second': 2}, {'first': 4, 'second': '-'}]

def mergedict(list1, list2, result = []): 
    if not list1 and not list2:
        return result
    temp_dict = dict()
    temp_dict["first"] = list1[0] if list1 else '-'
    temp_dict["second"] = list2[0] if list2 else '-'
    result.append(temp_dict)
    return mergedict(list1[1:], list2[1:], result)

print(mergedict([1, 7, 2, 4], [2, 5, 2])) # = [{'first': 1, 'second': 2}, {'first': 7, 'second': 5}, {'first': 2, 'second': 2}, {'first': 4, 'second': '-'}]
print(type(mergedict([1, 7, 2, 4], [2, 5, 2])[0])) # <class 'dict'>