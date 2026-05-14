# Given a string s, determine if it is a palindrome considering only alphanumeric characters and ignoring case.

# A. Pattern recognition
# Two pointers that need to move in opposite directions and check equality

# B. Optimal idea
# Initialize two pointers, left and right
# Initialize left pointer with 0 and right pointer with len(s)
# If any pointer in iteration if values at left or right pointers are not alphanumeric, skip the characters
# Check if the values at left and right pointers are equal
# If they are equal, move left pointer to the right and right pointer to the left
# Repeat until left pointer crosses right
# If at any state the values are not equal, return false
# Else return true
# Time Complexity - O(n)
# Space Complexity - O(1)

# C. Edge cases
# Empty string
# string with length 1
# String with odd length 
# String with even length
# String with non alphanumeric characters
# String with uneven case


# D. Clean Python implementation

def valid_palindrome(s):

    # Assuming empty string is palindrome, if not return false
    if len(s) == 0 or len(s) == 1:
        return True
    
    s = s.lower()

    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1


    return True
    