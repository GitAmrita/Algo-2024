# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
from typing import List


def countBits(n: int) -> List[int]:
    ans = list()
    index = 0
    while index <= n:
        ans.append(countABit(index))
        index += 1
    return ans


def countABit(index: int):
    count = 0
    while index > 0:
        count += index & 1
        index = index >> 1
    return count