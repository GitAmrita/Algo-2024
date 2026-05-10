from collections import defaultdict
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s: str, t: str) -> bool:
    words = defaultdict(int)
    if len(s) != len(t):
        return False
    for c in s:
        words[c] += 1
    for c in t:
        if c not in words:
            return False
        words[c] -= 1
        if words[c] == 0:
            del words[c]
    return len(words) == 0