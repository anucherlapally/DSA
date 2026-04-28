# Given two strings s and t, return True if t is an anagram of s, else False.


# A. Pattern Recognition
# an anagram of a string would need to contain all the letters appearing exactly the same amount of times as in the original string
# to check if two strings are anagrams, we would need to see if each letter of s is present in t and the same amount of times

# B. Brute Force
# Check if len of both strings are equal - if not return False
# Initiate seen array with len of t with elements as False
# Iterate through s in outer loop
# Iterate through t in inner loop (0, len(t)), if a letter matches and seen at that index is False, change it to True and move s forward
# If for any iteration in s, iteration in t ends without letter match and seen[index] as false, then break loop return False
# If iteration in s ends and seen is true throughout array, return True else False

# C. Optimal Approaches

# Give two possible optimal approaches:

# Sorting approach
#   If len of string not equal - return False
#   Sort both the strings O(nlogn)
#   Iterate through both of them and if at any index the letters do not match, they are not anagrams
#   If iteration ends, then anagrams

# Hashmap counting approach
#   If len of string not equal - return False
#   Initialize dict 1 
#   Iterate through s and add each letter to dictionary, increasing count whenever that character is encountered O(n)
#   Iterate through t and if letter is not in dict - return False O(n)
#   if letter in dict, decrease value count
#   if value count < 0, return False
#   For all keys in dict, check if any value is greater than 0 - return False O(n)
#   return True

# Compare them.
# Complexity
#   Sorting - O(nlogn)
#   Hashing - O(n)

# D. Edge Cases
#   Length of both lists not equal
#   Both lists empty
#   No common letter in both lists
#   Not all letters matching
#   All common letters with different frequencies

# E. Interview Communication Drill
# “Why is hashmap often preferred over sorting here?”
#   Hashmap is different than sorting because it's efficient with respect to time complexity
#   Space complexity will increase due to the addition of a dictionary, but the worst case is O(n) space complexity increase


def valid_anagram(s, t):

    if len(s) != len(t):
        return False
    
    char_map = {}

    for letter in s:
        char_map[letter] = char_map.get(letter, 0) + 1

    for letter in t:
        if letter not in char_map:
            return False
        
        char_map[letter] -= 1

        if char_map[letter] < 0:
            return False
        
    return True