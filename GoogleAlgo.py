class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        s = str(x)
        if is_negative:
            reversed_val = s[::-1]
            reversed_val = reversed_val[:-1]
            reversed_val = ['-'] + list(reversed_val)
            reversed_val = ''.join(reversed_val)
        else:
            reversed_val =  s[::-1]
        return self.signed_32_bit_integer(reversed_val)

    def signed_32_bit_integer(self, value):
        MIN_INT = - 2**31
        MAX_INT = 2**31
        try:
            res = int(value)
            if MIN_INT <= res <= MAX_INT:
                return res
            else:
                return 0
        except:
            return 0