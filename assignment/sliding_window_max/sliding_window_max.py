'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# wednesday - first pass
def sliding_window_max(nums, k):
    # returns max of the integers inside the window, sized k
    # using a for loop for the movement of the window through the array nums,
    # one array element at a time
    return [max(nums[i:(i + k)]) for i in range(len(nums) - k + 1)]

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
