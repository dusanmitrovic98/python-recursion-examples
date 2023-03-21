# Define function "product", which calculates the product of a list of sublists (A) and a list of numbers (B). Consider that the number of sublists in
# list A equal to the length of list B. The function returns a list that has as many elements as the length
# input lists. The Nth element of the output list represents the sum of all elements of the Nth sublist of list A which in
# previously multiplied by the Nth element in lists B. The use of loops and the sum function is prohibited.
# Example: product([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]) = [6, 30, 72]

def product(A, B):
    if not A and not B:
        return []
    elif not A and B:
        return 0
    elif isinstance(A[0], int):
        return (A[0] + product(A[1:], B))
    elif isinstance(A[0], list):
        sum = product(A[0], B)
        prod = sum * B[0]
        return [prod] + product(A[1:], B[1:])


print(product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))
