#  Pattern Recognition
#   Sorting is one method by which consecutive sequence can be found easily
#   I don't know an method that's more optimal than this

# Brute Force
#   For each element in the outer loop, I'll see if the next or prev element exists, if yes, I'll take the existing element and run an iterative loop checking for consecutive elements until none are found.
#   update the counter and move to the other element
#   I'll use a seen array to keep track of elements already found and skip them  

# Final Optimal Algorithm
# Loop through the array
# Check if the element is the start of the sequence with if x - 1 exists
#   if it exists - skip because x is not a sequence start
#   else start another loop to check if x + 1, +2, + 3 exists until it doesn't, update counter if greater

# Complexity
# Time - O(n) - worst case is if all the elements in the array are part of consecutive sequence then loop runs O(2n) - O(n)
# Space - O(n) - uses set for fast element retrieval

# Invariant
# During sequence expansion, what do:
# current_num - the element at the sequence
# current_length - length until sequence expansion - if at x + 4 and exists, then cur_length = 5

def longest_consecutive_seq(nums):

    num_set = set(nums)
    max_length = 0

    for num in num_set:

        if num - 1 in num_set:
            continue

        current_num = num
        current_length = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length

# Sorting is not accepted for this constraint because sorting takes o(nlogn) and the constraint specifically asks for an O(n) solution