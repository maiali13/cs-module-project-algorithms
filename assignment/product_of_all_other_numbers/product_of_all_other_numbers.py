'''
Input: a List of integers
Returns: a List of integers
'''
# wednesday - first pass
# [1, 7, 3, 4] -->
# [7*3*4, 1*3*4, 1*7*4, 1*7*3] -->
# [84, 12, 28, 21]
def product_of_all_other_numbers(arr):
    prods = []
    for i, j in enumerate(arr):
        # make copy of arr
        temp = arr.copy()
        # remove the index number
        temp.pop(i)
        prod = 1
        for x in temp:
            prod *= x # assignment operators make me feel like a real programmer ᕦ(^‿^)ᕤ 
        # append partial products to the array
        prods.append(prod)

    return prods

# thursday - improvements
# not sure how I can improve this alg...
# runtime is O(n*(n-1))?**
# **unless .copy() counts as an O(n) operation

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
