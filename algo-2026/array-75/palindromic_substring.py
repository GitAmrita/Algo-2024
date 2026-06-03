# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
def countSubstrings(s: str) -> int:
    res = 0
    def get_palin_count(left, right):
        count = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            else:
                break
        return count
    for i in range(len(s)):
        res += get_palin_count(i, i) + get_palin_count(i, i + 1)
    return res