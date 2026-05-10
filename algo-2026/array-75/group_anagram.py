from collections import defaultdict
from typing import List

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
# Input: strs = [""]
# Output: [[""]]
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:
        return [strs]
    sorted_list = []
    for w in strs:
        sorted_list.append( "".join(sorted(w)) )
    
    words = defaultdict(list)
    for i in range(len(sorted_list)):
        words[sorted_list[i]].append(strs[i])
    return list(words.values()) 