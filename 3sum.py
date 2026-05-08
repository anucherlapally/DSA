# A. Pattern Recognition
# Sorting helps in keeping track of how the sum is changing as we move left or right
# After sorting, with a fixed element we can have two pointers moving left and right
# If the sum of the three elements is greater than zero, move the right pointer
# else move the left pointer, if sum == 0, add the triplet to the output array
# Once left and right pointers cross each other, that iteration ends
# Complexity - O(n2)

# B. Brute Force
# Naive approach would use three loops
# and check if a such a triplet exists and if so add to the output array
# Complexity - O(n3)

# C. Optimal Insight
# We reduce 3sum to repeated 2sum by sorting

# D. Pointer Movement Logic (Critical)

# After sorting:
# We move the left pointer if sum is less than zero because we need to increase the sum and movement to the left has larger numbers
# We move the right pointer if sum is greater than zero because we need to decrease the sum and movement to the right has smaller numbers

# E. Duplicate Handling
# How do we avoid duplicate triplets?
# Since the elements are sorted, if we skip the same elements for fixed pointer, we can avoid duplicate triplets.
# We would also need to skip same left and right pointers

# F. Invariant

# At any moment during inner loop:

# i would always be to the left of both left and right pointers
# left pointer should always be on the left of the right pointer
# The loop would run until i < len(nums) - 3


def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):

        # skip duplicate fixed values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result
        


    


