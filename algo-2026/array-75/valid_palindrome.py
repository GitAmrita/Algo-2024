# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s: str) -> bool:
    lower_alpha_numeric = (''.join(c for c in s if c.isalnum())).lower()
    left = 0
    right = len(lower_alpha_numeric) - 1
    while left < right:
        if lower_alpha_numeric[left] != lower_alpha_numeric[right]:
            return False
        left += 1
        right -= 1
    return True

