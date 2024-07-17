from GoogleAlgo import Solution, RangeModule
from MediumAlgo import  *
from DSACrashCourse.ArraysAndStrings import *


# rooms=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# result = wallsAndGates(rooms=rooms)
# print(result)

# sol = Solution()
# # -2147483649 is outside the range of signed 32 bit int
# res = sol.reverse(-2147483649) 
# print(res)

# print(sol.generateParenthesis(n = 2))

# obj = RangeModule()
# obj.addRange(10,20)
# obj.addRange(30,40)
# obj.addRange(25,70)
# obj.addRange(32,48)
# param_2 = obj.queryRange(14,89)
# obj.removeRange(32,39)

chapter_1 = ArraysAndStrings()
# res = chapter_1.reverse_string( ["h","e","l","l","o"])
# res = chapter_1.sorted_squares([])
# res = chapter_1.longest_subarray_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
# res = chapter_1.find_length("1111011101110111")
# res = chapter_1.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
res = chapter_1.find_best_subarray([10, 5, 2, 30], 3)