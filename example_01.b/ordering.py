# Define function 'ordering', which combines 2 lists of numbers into one list consisting of tuple objects that have three elements. 
# The first element of the resulting collection is an element of the first list, the second is an element of the 
# second list, and the third is either 'Yes' if the second list element is twice as large as the first list element,
# or 'No' if it is not. The length of the list is the dimension of the longer of the two input lists. The nth tuple 
# data of the resulting collection consists of the nth numbers from both input lists, where the smaller and larger 
# numbers from both lists should be at the first and second positions, respectively.

# The shorter input list is filled with the number 0 at the end until both lists are of the same length. The use of loops is prohibited.

# Example: ordering([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 'Yes'), (7, 5, 'No'), (2, 2, 'No'), (4, 0, 'No')]

# Without recursion
# def ordering(list1, list2): 
#     if len(list1) > len(list2):
#         list2 += [0] * (len(list1) - len(list2))
#     else: 
#         list1 += [0] * (len(list2) - len(list1))
    
#     combined_list = [(x, y) for x, y in zip(list1, list2)]

#     return [(x, y, 'Yes' if y == x*2 else 'No') for x, y in combined_list]

def ordering(list1, list2, result_list = []):
