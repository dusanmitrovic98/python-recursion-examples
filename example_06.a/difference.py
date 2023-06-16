# Define function "difference", which takes two lists (of any data type) as input,
# and returns a list composed of all the elements from the first list that are not
# in the second list. Example: difference([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"].

def difference(listA, listB):
    if not listA:
        return []
    elif not isinstance(listA, list):
        if listA not in listB:
            return [listA]
        else:
            return []
    else:
        return difference(listA[0], listB) + difference(listA[1:], listB)

print(difference([1, 4, 6, "2", "6"], [4, 5, "2"]))
