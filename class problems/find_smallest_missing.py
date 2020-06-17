def find_smallest_missing(arr):
    # edge case: deal with edge case where 0 is missing 
    # check to make sure that 0 is at the front of the array 
    if arr[0] != 0:
        return 0
    # edge case: if no elements are missing, return the element right 
    # after the last element  

    # loop through the arr
    # need to loop till len(arr)-1 since we're checking
    # for the i+1 element 
    for i in range(len(arr)-1):
        # check the element adjacent to the current 
        # make sure that the adjacent element == current + 1
        if arr[i+1] != arr[i] + 1:
            # if adjacent element != current + 1
            # then we know that current + 1 _should_ be there 
            # but it isn't 
            # so return current + 1 
            return arr[i] + 1

    # if we get out of the for loop, then we didn't find any missing 
    # elements 
    return arr[-1] + 1

A = [0, 1, 2, 3, 4, 5, 6]
print(find_smallest_missing(A))