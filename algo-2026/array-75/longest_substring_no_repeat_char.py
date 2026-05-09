# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0
    seen = set()
    longest = 0
    for i in range(len(s)):
        if s[right] not in seen:
            seen.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        else:
            for j in range(left, right + 1):
                if s[left] == s[right]:
                    left += 1
                    right += 1
                    break
                else :
                    seen.remove(s[left])
                    left += 1
    return longest