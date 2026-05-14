# Given a string s, find the length of the longest substring without repeating characters.

# A. Pattern Recognition
# This is a sliding window problem because we increase the window as long as there are no repeating characters and when one occurs,
# we decrease the window and slide it after the repeating character

# B. Brute Force
# Take every possible substring and check for repeating characters
# Start with length 2 till length of the string
# Populate substrings and discard if repeating characters exist
# 

# C. Sliding Window Insight

# What does the window represent?

# When do we expand?
# When do we shrink?

# D. Duplicate Logic (Critical)

# Suppose current character already exists in window.

# What exactly must happen?

# E. Invariant

# At every step, what property must the window maintain?