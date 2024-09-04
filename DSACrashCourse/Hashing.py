from collections import Counter, defaultdict
import math
import string
from typing import List
class Hashing:

    def is_pangram(self, sentence: str) -> bool:
        '''
        A pangram is a sentence where every letter of the English alphabet appears at least once. Given a string sentence
        containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
        '''
        alphabets =  set([s for s in sentence])
        for ch in string.ascii_lowercase:
            if ch not in alphabets:
                return False
        return True
    
    def mission_number(self, nums: list) -> int:
        '''
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
        missing from the array.
        '''
        max_num = len(nums)
        all_nums =  set([s for s in nums])
        for i in range(max_num + 1):
            if i not in all_nums:
                return i
            
    def count_elements(self, arr: list) -> int:
        '''
        Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
        If there are duplicates in arr, count them separately.
        Input: arr = [1,2,3] Output: 2
        '''
        ans = 0
        all_nums =  set([s for s in arr])
        for n in arr:
            if n + 1 in all_nums:
                ans += 1
        return ans
    
    def find_longest_substring(self, s, k):
        '''
        You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct
        characters.
        For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
        '''
        counts = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            print(ans)
            return ans
        
    def intersection(self, nums: List[List[int]]) -> List[int]:
        '''
        Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.
        For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4].
        3 and 4 are the only numbers that are in all arrays.
        '''
        ans = []
        counts = defaultdict(int)
        for i in range(len(nums)):
            arr = nums[i]
            for j in range(len(arr)):
                counts[arr[j]] += 1
                if counts[arr[j]] == len(nums):
                    ans.append(arr[j])
        print(sorted(ans))
        return sorted(ans)
    
    def are_occurrences_equal(self, s: str) -> bool:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        for val in freq.values():
            s.add(val)
        return len(s) == 1

    def subarray_sum(self, nums, k) -> int:
        '''
        Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
        [1, 2, 1, 2, 1], k = 3 output = 4 [1,2][2,1][1,2][2,1]
        [1, 3, 4, 6, 7]
        '''
        freq = 0
        curr = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for num in nums:
            curr += num
            freq += prefix[curr - k]
            prefix[curr] += 1
        print(freq)
        return freq
    
    def nice_subarray(self, nums, k) -> int:
        '''
        Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.
        For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].
        '''
        freq = 0
        odds = 0
        odd_count = defaultdict(int)
        odd_count[0] = 1
        for num in nums:
            if num % 2 == 1:
                odds += 1
            freq += odd_count[odds - k]
            odd_count[odds] += 1
        print(freq)
        return freq
    
    def zero_or_one_loss(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
        Return a list answer of size 2 where:
        answer[0] is a list of all players that have not lost any matches.
        answer[1] is a list of all players that have lost exactly one match.
        The values in the two lists should be returned in increasing order.
        Note:
        You should only consider the players that have played at least one match.
        The testcases will be generated such that no two matches will have the same outcome.
        Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]] Output: [[1,2,10],[4,5,7,8]]
        '''
        all_players = set()
        no_loss  = []
        one_loss = []
        lost_playes = defaultdict(int)
        output = []
        for match in matches:
            all_players.add(match[0])
            all_players.add(match[1])
            lost_playes[match[1]] += 1
        for p in all_players:
            if lost_playes[p] == 0:
                no_loss.append(p)
            if lost_playes[p] == 1:
                one_loss.append(p)
        no_loss =  sorted(no_loss)
        one_loss = sorted(one_loss)
        output.append(no_loss)
        output.append(one_loss)
        print(output) 
        return output
    
    def largest_unique_number(self, nums) -> int:
        '''
        Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
        '''
        freq = defaultdict(int)
        ans = -1
        for num in nums:
            freq[num] += 1
        for key, value in freq.items():
            if value == 1:
                ans = max(ans, key)
        return ans
    
    def instances_of_word(self, text) -> int:
        '''
        Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
        You can use each character in text at most once. Return the maximum number of instances that can be formed.
        '''
        freq = Counter(text)
        ans = 0
        while True:
            for ch in 'balloon':
                if freq[ch] == 0:
                    return ans
                else:
                    freq[ch] -= 1
            ans += 1
        return ans
    
    def find_max_length(self, nums: List[int]) -> int:
        '''
        Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
        input [0, 0, 1, 1, 0, 0, 0, 1, 1, 0 ,1 ,1 ,1 ] output 12 [0, 0, 1, 1, 0, 0, 0, 1, 1, 0 ,1 ,1 ]
        [0,0,1,0,0,0,1,1]
        [-1,-2,-1,-2,-3,-4,-3,-2]
        '''
        sum = 0
        ans = 0
        dic = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                sum += -1
            else:
                sum += nums[i]
            if sum not in dic.keys():
                dic[sum] = i
            else:
                len_of_sub = i - dic[sum]
                ans = max(ans, len_of_sub)
        print(ans)
        return ans
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
        '''
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
        print(anagrams.values())
        return anagrams.values()
    
    def minimum_card_pickup(self, cards: List[int]) -> int:
        '''
        Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate.
        If the array has no duplicates, return -1.
        [1, 2, 6, 1, 2, 1, 1] 1 -> 0, 3, 5, 6    2 -> 1, 4 
        '''
        def _get_lowest_difference(nums) -> int:
            ans = math.inf
            for i in range(len(nums) -1, 0, -1):
                diff = nums[i] - nums[i - 1]
                ans = min(ans, diff)
            return ans
    
        pos = defaultdict(list)
        ans = math.inf
        for i in range(len(cards)):
            pos[cards[i]].append(i)
        for key, values in pos.items():
            lowest = _get_lowest_difference(values)
            ans = min(ans, lowest)
        return -1 if ans == math.inf else ans
    
    def maximum_sum(self, nums: List[int]) -> int:
        '''
        Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same
        digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.
        input [23, 41, 76, 94, ] output 76 + 94 [-15, 60, 91, 82]
        '''
        def get_biggest_two_numbers_sum(lst) -> int:
            if len(lst) == 1:
                return - math.inf
            lst.sort(reverse=True)
            return lst[0] + lst[1]
            
        holder = defaultdict(list)
        ans = -math.inf
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            holder[digit_sum].append(num)
        for values in holder.values():
            biggest_sum = get_biggest_two_numbers_sum(values)
            ans = max(ans, biggest_sum)
        if ans == -math.inf:
            ans = -1
        print(ans)
        return ans
    
    def equal_pairs(self, grid: List[List[int]]) -> int:
        '''
        Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column,
        and R and C are equal if we consider them as 1D arrays.
        imput [[3,2,1], [1,7,6], [2,7,7]] output =  [r=2, c=1]
        3 2 1  3 3 3 
        1 7 6  3 3 3
        2 7 7  3 3 3
        '''
        pairs = 0
        dic = defaultdict(list)
        for i in range(len(grid)):
            dic[tuple(grid[i])].append(i)

        num_columns = len(grid[0])
        for col in range(num_columns):
           column_values = [grid[row][col] for row in range(len(grid))]
           tup = tuple(column_values)
           if tup in dic:
               pairs += len(dic[tup])
        return pairs
    
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        freq_counter = Counter(magazine)
        for c in ransomNote:
            jj = freq_counter.get(c, None)
            if jj is None or jj == 0:
                return False
            else:
                freq_counter[c] = freq_counter[c] - 1
        return True
    
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        count = 0
        for c in jewels:
            jewels_set.add(c)
        for s in stones:
            if s in jewels_set:
                count += 1
        return count
    
    def length_of_longest_substring(self, s: str) -> int:
        '''
         s = "pwpkew"
        '''
        seen = set()
        res = 0
        for left in range(len(s) - 1):
            seen.add(s[left])
            for right in range(left + 1, len(s)):
                if s[right] not in seen:
                    seen.add(s[right])
                    right += 1
                else:
                    length = len(seen)
                    res = max(res, length)
                    seen.clear()
                    break
        print(max(res, len(seen)))
        return max(res, len(seen))
    
    def destination_city(self, paths:List[List[str]]) -> str:
        '''
        You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
        It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
        Input: paths = [["B","C"],["D","B"],["C","A"]]   Output: A
        '''
        seen = set()
        for path in paths:
            seen.add(path[0])
        for path in paths:
            if path[1] not in seen:
                return path[1]

    def is_path_crossing(self, path: str) -> bool:
        '''
        Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west,
        respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
        Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
        Input: path = "NES" Output: false 
        '''
        points = set()
        curr_x = 0
        curr_y = 0
        points.add((curr_x, curr_y))
        for p in path:
            if p == 'N':
                curr_y += 1
            elif p == 'S':
                curr_y -= 1
            elif p == 'E':
                curr_x += 1
            else:
                curr_x -= 1
            if (curr_x, curr_y) in points:
                return True
            else:
                points.add((curr_x, curr_y))
        return False
    
    def max_frequency_elements(self, nums: List[int]) -> int:
        '''
        You are given an array nums consisting of positive integers. Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
        The frequency of an element is the number of occurrences of that element in the array
        Input: nums = [1,2,2,3,1,4] Output: 4
        Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
        So the number of elements in the array with maximum frequency is 4.
        '''
        dic = Counter(nums)
        sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items)
        count = 0
        first_key, first_value = list(sorted_dict .items())[0]
        for val in sorted_dict.values():
            if val == first_value:
                count += 1
            else:
                break
        return count * first_value
    
    def findLucky(self, arr: List[int]) -> int:
        '''
        Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
        Return the largest lucky integer in the array. If there is no lucky integer return -1
        '''
        res = -1
        freq = Counter(arr)
        for key, value in freq.items():
            if key == value:
                res = max(res, key)
        return res
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''
        Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
        Input: arr = [1,2,2,1,1,3] Output: true
        Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
        '''

        freq = Counter(arr)
        unique = set(freq.values())
        return len(unique) == len(freq.keys())
    
    def frequencySort(self, s: str) -> str:
        '''
        Given a string s, sort it in decreasing order based on the frequency of the characters.
        The frequency of a character is the number of times it appears in the string.
        Return the sorted string. If there are multiple answers, return any of them.
        '''
        freq = Counter(s)
        ans = ''
        sorted_freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))

        for key, value in sorted_freq.items():
            val = key * value
            ans += val
        return ans
    
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''
        Input: nums = [1,2,3,1,2,3,1,2], k = 2 Output: 6
        '''
        freq = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[nums[right]]> k:
                freq[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        [1,2,3,1,1,3]
        Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        '''
        count = 0
        index = defaultdict(list)
        for i in range(len(nums)):
            index[nums[i]].append(i)
        for value in index.values():
            count += len(value) if len(value) > 1 else 0
        return count









               
         

            



    






    




    











    



        






        

