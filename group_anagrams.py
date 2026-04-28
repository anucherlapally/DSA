# Given an array of strings strs, group the anagrams together.

# A. Pattern Recognition
# group strings that are anagrams 
# identify anagrams - words with identical frequency distribution

# B. Brute Force - complexity O(n2 * klogk) [n - len of strs, k - len of words]
# For each string:
#     compare with every other string
#     check if they are anagrams (by sorting or counting)
#     group them

# C. Key Insight
# Hashmap key could be sorting-based key or frequency-based key

# Give two approaches:
# Sorting-based key
#   Initialize a hash map
#   Iterate through strs O(N)
#       sort the string and check if sorted string present in hashmap, if yes append original string to output list O(k logk)
#       else add the sorted string as key and [original string] as value
#   Iterate through dictionary and append values to an output list O(m)
#   Return output list
# N - len of strs, k - len of words, m - number of unique sorting keys
# Complexity - O(n . k logk)

# Frequency-based key
#   Initialize a hash map
#   Iterate through strs - O(N)
#       Initialize another hashmap
#       Iterate through string and count the characters - O(k)
#       Iterate through inner hashmap - create a frequency string - char1count1char2count2
#       Check if freq string in the outer hashmap, if yes append original string to value
#       else add new key with freq string and value as [original string]
#   Iterate through dictionary and append values to an output list O(m)
#   return output list
#   N - len of strs, k - len of words, m - number of unique freq keys
# Complexity - O(N . k)

# D. Tradeoff
# Sorting would be acceptable if len of words is less

# E. Invariant
# At any point, hashmap would contain sorting or frequency keys and values as list of anagrams


#sorting based key
from collections import defaultdict

def group_anagrams(strs):

    word_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        word_map[key].append(word)

    return list(word_map.values())

