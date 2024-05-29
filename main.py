from GoogleAlgo import Solution
from MediumAlgo import  *


# rooms=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# result = wallsAndGates(rooms=rooms)
# print(result)

sol = Solution()
# -2147483649 is outside the range of signed 32 bit int
res = sol.reverse(-2147483649) 
print(res)