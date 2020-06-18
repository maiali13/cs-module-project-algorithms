'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# wednesday - first pass
def single_number(arr):
    no_dupes = []
    # loop through the array
    for i in arr:
        if i not in no_dupes:
            no_dupes.append(i)
        # remove any number in arr that has a duplicate from no_dupes array
        else:
            no_dupes.remove(i)
    # once done, the only number left in no_dupes should be our odd number out
    return no_dupes[0]

# thursday - improvements
# first pass solution already O(n)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")