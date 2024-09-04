from DSACrashCourse.Hashing import Hashing
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
# res = chapter_1.find_best_subarray([10, 5, 2, 30, 6, 12, 78], 3)
# res = chapter_1.find_max_avg_subarray([1,12,-5,-6,50,3], 4)
# res = chapter_1.max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0], 2)
# res = chapter_1.running_sum([1,1,1,1,1])
# res = chapter_1.k_radius_avg([7,4,3,9,1,8,5,2,6], 3)
# res = chapter_1.reverse_words_in_string('     ')
# res = chapter_1.reverse_only_letters("a-bC-dEf-ghIj")
# res = chapter_1.get_min_common([1,2,8,12,32,47], [9,11,12,14,19,25,29,31,])
# res = chapter_1.move_zeros([0,1,0,3,12])
# res = chapter_1.reverse_prefix_of_word("abcdefd", "d")
# res = chapter_1.minimum_length_subarray(7, [2,3,1,2,4,3])
# res = chapter_1.max_vowels('leetcode', 3)
# res = chapter_1.equal_substring('krrgw', 'zjxss', 19)
# res = chapter_1.largest_altitude([-5,1,5,0,-7])
# res = chapter_1.pivot_index([2,1,-1])

chapter_2 = Hashing()
# res = chapter_2.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])
# res = chapter_2.subarray_sum([1, 2, 1, 2, 1], 3)
# res = chapter_2.nice_subarray([1, 1, 2, 1, 1, 3], 3)
# res = chapter_2.zero_or_one_loss([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
# res = chapter_2.find_max_length([0,1])
# res = chapter_2.group_anagrams(["eat","tea","tan","ate","nat","bat"])
# res = chapter_2.minimum_card_pickup([1, 2, 6, 1, 2, 1, 1])
# res = chapter_2.equal_pairs([[3,2,1], [1,7,6], [2,7,7]])
# res = chapter_2.length_of_longest_substring('aab')
# res = chapter_2.max_frequency_elements([1,2,2,3,1,4])
# res = chapter_2.frequencySort("tree")
# res = chapter_2.maxSubarrayLength([1,4,4,3, 5, 7, 9], 1)
res = chapter_2.numIdenticalPairs([1,2,3,1,1,3])