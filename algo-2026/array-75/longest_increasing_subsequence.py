# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [None] * len(nums)
    dp[0] = 1
    for index in range(1, len(nums)):
        max_len = float('-inf')
        for j in range(index -1, -1, -1):
            if nums[index] > nums[j]:
                max_len = max(max_len, dp[j] + 1)
            else:
                max_len = max(max_len, 1) 
        dp[index] = max_len
    return max(dp)