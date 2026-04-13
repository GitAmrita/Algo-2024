# Add 2 numbers a=6 b=3 without using + and - operators
def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    max_positive_32_bit_int = 0x7FFFFFFF
    while b != 0:
        carry = ((a & b) << 1) & mask
        a = (a ^ b) & mask
        b = carry
    if a > max_positive_32_bit_int:
        a = ~(a ^ mask)
    return a