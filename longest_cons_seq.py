# Given an array of integers, return the length of the longest consecutive sequence.

# Example:
# [100,4,200,1,3,2]
# Output:
# 4
# Because sequence is 1,2,3,4
# Requirements:
# Better than O(n log n) if possible.


#Brute force approach -
# sort the array 
# intialize variables - max_seq, curr_seq
# check if diff of curr and next integer is 1 
#       if yes increment curr_seq
#       else take the max of max_seq, curr_seq for max_seq and set curr_seq = 0
# loop until end of list

# complexity 
#  sort - O(n log n)
#  single pass - O(n)
#  comparison - O(1) * n 
# Brute force final complexity - O(n log n)

# Better approach 
# Initialize a dictionary - look_up
# key - element, value - [0, False] 
# populate the dictionary by making a pass over the list 
# iterate over elements in list
# for element in list, 
#       if dict[key][1] is true then continue,
#       else: 
#               make index of the boolean element as True 
#               if x - 1 or x + 1 exists  
#                   then increment the value
#              
#               take the new element and repeat              
#


def get_longest_consecutive_sequence(nums):

    look_up = {}
    max_seq = 0

    #Complexity - O(n)
    for num in nums:
        look_up[num] = look_up.get(num, [0, False]) 


    for num in nums: #O(n)
        if look_up[num][1]: #O(1)
            continue

        look_up[num][1] = True
        prev_value, next_value = num - 1, num + 1
        while prev_value in look_up and not (look_up[prev_value][1]):
            look_up[num] += 1
            look_up[prev_value][1] = True 
            prev_value -= 1

        while next_value in look_up and not (look_up[next_value][1]):
            look_up[num] += 1
            look_up[next_value][1] = True
            next_value += 1

        max_seq = max(max_seq, look_up[num])


    return max_seq

#Complexity - O(n)