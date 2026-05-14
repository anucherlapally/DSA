# A. Pattern Recognition
# Sorting does not work here because for the area we need the distance between the pointers as well along with the smallest height
# We need to move the small pointer because the large pointer can contribute to the maximum area better than the small pointer

# B. Brute Force
# Use two loops, take all the possible areas and output the maximum area
# Time Complexity - O(n^2)
# Space Complexity - O(1)

# C. Optimal Insight
# Two pointers can work because we calculate the area using the heights, moving one pointer from left and another from right covers all the possible areas

# D. Critical Greedy Reasoning (Most Important)
# Suppose:
# left_height < right_height
# Why is it safe to move the left pointer?
# Area is calculated with the minimum heights of the two pointers, so moving the smallest height assures that the maximum height can still be obtained
# This is the heart of the problem.

# E. Invariant
# At every step, the height of the smallest pointer and the distance between the two pointers determine the area.
# We are trying to optimize the length and the width (distance between the pointers and the length of the smallest pointer)


def container_with_most_water(heights):

    left, right = 0, len(heights) - 1
    max_area, curr_area = 0, 0

    while left < right:
        curr_area = min(heights[left], heights[right]) * (right - left)
        max_area = max(curr_area, max_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


# moving the taller pointer is never useful while shorter pointer remains unchanged because we're reducing the width anyway and if taller pointer is moved, 
# we're reducing the chances of obtaining the maximum area since for length, we take the minimum of the two pointers