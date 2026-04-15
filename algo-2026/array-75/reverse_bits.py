# Reverse bits of a given 32 bits signed integer.
# Example 1:
# Input: n = 43261596
# Output: 964176192

def reverseBits(self, n: int) -> int:
    result = 0
    for i in range(32):
        result <<= 1
        rightmost_bit = n & 1
        result = result | rightmost_bit
        n = n >> 1
    return result