# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
from collections import defaultdict

def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    right = 0
    freq = defaultdict(int)
    while right < len(s):
        win_len = right - left + 1
        freq[s[right]] += 1
        max_freq = max(freq.values())
        replacements = win_len - max_freq
        if replacements > k:
            freq[s[left]] -= 1
            left += 1
            right += 1
        else:
            right += 1
    return (right - left)