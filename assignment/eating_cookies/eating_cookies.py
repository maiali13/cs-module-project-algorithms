'''
Input: an integer
Returns: an integer
'''
### wednesday - first pass ###

# this question is similar to the Fibonacci sequence question,
# https://leetcode.com/problems/fibonacci-number/
# except we must sum the previous 3 elements instead of the previous 2

# should be recursive and can utilize chache 
# cache would have to be given in the input

# def eating_cookies(n):
#     # base case - 0 cookies
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # only 1 cookie
#     elif n == 1:
#         return 1
#     # 2 cookies
#     elif n == 2:
#         return 2
#     # 3+ cookies
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# this solution is slow and too high runtime (O(3^n)), can definetly be optimized
# probably implementing a cache and just using math instead of callback
# runs well on small inputs
# has issues with the large test but will optimize tomorrow 

### thursday - improved solution ###

# the cache allows us to save our work 
# cache is a dictionary where keys is the n, value is the answer 

def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache 
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our 
        # recursive logic to calculate it, and then save the answer in our 
        # cache for future uses 
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache) 
    return cache[n]

# Runtime: O(n)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100
    cache = {i: 0 for i in range(num_cookies+1)}
    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")
