# Given an integer array nums and integer target, return indices of two numbers such that they add to target.

#Brute force explanation
# Initialize two loops - outer and inner
# For every element in the outer loop, check all the elements (not the current element) and see if they are a pair

def two_sum(nums, target):

    seen = {}

    for index,num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], index]
        else:
            seen[num] = index

    return None

# At the start of each iteration, the hashmap contains all the elements that are already seen and their indices