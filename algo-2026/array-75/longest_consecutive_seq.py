# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List
def longestConsecutive(self, nums: List[int]) -> int:
    unique = set(nums)
    max_len = 0
    for n in unique:
        if (n - 1) not in unique:
            local_max = 1
            while (n + 1) in unique:
                local_max += 1
                n = n + 1
            max_len = max(max_len, local_max)
    return max_len