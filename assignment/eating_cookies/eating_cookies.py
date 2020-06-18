'''
Input: an integer
Returns: an integer
'''
# wednesday - first pass

# this question is similar to the Fibonacci sequence question,
# https://leetcode.com/problems/fibonacci-number/
# except we must sum the previous 3 elements instead of the previous 2

# should be recursive and can utilize chache 
# cache would have to be given in the input

def eating_cookies(n):
    # base case - 0 cookies
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # only 1 cookie
    elif n == 1:
        return 1
    # 2 cookies
    elif n == 2:
        return 2
    # 3+ cookies
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# this solution is slow and too high runtime, can definetly be optimized
# probably implementing a cache and just using math instead of callback
# runs well on small inputs
# has issues with the large test but will optimize tomorrow 
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
