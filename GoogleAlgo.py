import bisect
from typing import List


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

    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
        
class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        subtrack = []
        if self.is_even_number(start):
            subtrack.append(left)
        if self.is_even_number(end):
            subtrack.append(right)
        self.track[start:end] = subtrack
        

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
        return True
        

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)


    def is_even_number(self, num) -> bool:
        return num % 2 == 0