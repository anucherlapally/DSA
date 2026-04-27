# Given an integer array nums, return True if any value appears at least twice, else False.


def contains_dup(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
        
    return False
