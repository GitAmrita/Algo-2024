# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

def hammingWeight(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1
        print(f"n: {bin(n)[2:]}, count: {count}, n & 1: {bin(n & 1)[2:]}")
        n = n >> 1
    return count