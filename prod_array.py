# Given an integer array nums, return an array answer such that:
# answer[i] = product of all elements of nums except nums[i]


# A. Pattern Recognition
# We need the values of all the elements to the left and right of the current element
# This suggests a prefix and suffix elements - we need the product of prefix and suffix from the current element

# B. Brute Force
# Naive approach would be to loop through the array and take the element as product at each iteration O(n2)
# Another approach would be to take the product of all the elements in array and perform division with the current element O(n)

# C. Key Insight (Core)

# Explain how prefix and suffix products help.

# Be precise:
# what is prefix[i] - product of all the elements left of i
# what is suffix[i] - product of all elements right of i

# D. Optimal Plan (Two-Pass Version)
# Describe:
# First pass (what are you computing?)
#   initialize curr_prod = 1
#   start iteration from left till end
#   insert at output[i] = curr_prod
#   at each iteration update curr_prod *= curr_element
# Second pass (how do you combine?)
#   intialize curr_prod = 1
#   start iteration from right till beginning 
#   output[i] *= curr_prod
#   update curr_prod *= curr_element

# E. Invariant (Critical)

# At index i, what does your output array already contain during:
# first pass
#   product of elements to the left
# second pass
#   product of elements to the right


def prod_array_except_self(nums):

    curr_prod = 1
    res = [1] * len(nums)

    for i in range(len(nums)):
        res[i] = curr_prod
        curr_prod *= nums[i]

    curr_prod = 1

    for i in range(len(nums) - 1, -1, -1):
        res[i] *= curr_prod
        curr_prod *= nums[i]

    return res


# What happens when input contains zeros?

# Give 3 cases:

# no zero
#   the output array contains all the products with no zeros
# one zero
#   one element will contain one number other than zero, rest all are zeroes
# multiple zeros
#   the entire output array is zero