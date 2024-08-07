from typing import List
import math


class ArraysAndStrings:
    # Write a function that reverses a string.
    # The input string is given as an array of characters s.
    # You must do this by modifying the input array in-place with O(1) extra memory.
    def reverse_string(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        print(s)

    def sorted_squares(self, nums: List[int]) -> List[int]:
        # Given an integer array nums sorted in non-decreasing order, return an array of the squares 
        # of each number sorted in non-decreasing order.
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        print(result)
        return result
    
    def longest_subarray_sum(self, nums: List[int], k: int):
        #  Given an array of positive integers nums and an integer k, find the length of the longest 
        # subarray whose sum is less than or equal to k
        # nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8
        left = 0
        right = 0
        curr = 0
        answer = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            answer = max(answer, right - left + 1)
        print(answer)
        return answer

    
    def find_length(self, s: str):
        #  You are given a binary string s (a string containing only "0" and "1"). You may choose up to one 
        # "0" and flip it to a "1". What is the length of the longest substring achievable that contains only 
        # "1"?
        # s = "1 1 0 1 1 0 0 1 1 1" => 5
        left = 0 
        right = 0
        num_of_0 = 0
        answer = 0
        for right in range(len(s)):
            if s[right] == '0':
                num_of_0 += 1
            while num_of_0 > 1:
                if s[left] == '0':
                    num_of_0 -= 1
                left += 1
            answer = max(answer, right - left + 1)
        print(answer)
        return answer
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Given an array of positive integers nums and an integer k, return the number of subarrays where the 
        product of all the elements in the subarray is strictly less than k.

        For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8.
          The subarrays with products less than k are:

        [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
        '''
        if k <= 1:
            return 0
        left = 0
        right = 0
        answer = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            answer += right - left + 1
        print(answer)
        return answer
    
    def find_best_subarray(self, nums, k):
        '''
        Given an integer array nums and an integer k, find the sum of the subarray with the largest sum 
        whose length is k.
        '''
        curr = 0
        for i in range(k):
          curr += nums[i]
    
        ans = curr
        for i in range(k, len(nums)):
          curr += nums[i] - nums[i - k]
          ans = max(ans, curr)
        print(ans)
        return ans
    
    def find_max_avg_subarray(self, nums, k) -> float:
        '''
        Find a contiguous subarray whose length is equal to k that has the maximum average value
        and return this value. Any answer with a calculation error less than 10-5 will be accepted.
        nums = [1,12,-5,-6,50,3], k = 4
        '''
        sum = 0
        for i in range(k):
            sum += nums[i] 
        avg = sum/k
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            local_avg = sum / k
            avg = max(avg, local_avg)
        print(avg)
        return avg
    
    def max_consecutive_ones(self, nums, k) -> int:
        '''
        Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6
        Explanation: [1,1,1,0,0,1,1,1,1,1,1]
        '''
        left = 0
        ans = 0
        count_0 = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_0 += 1
            while count_0 > k:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            ans = max (ans, right - left + 1)
        print(ans)
        return ans
    
    def running_sum(self, nums) -> list[int]:
        '''
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
        Input: nums = [1,1,1,1,1]
        Output: [1,2,3,4,5]
        '''
        ans = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            ans[i] = s
        print(ans)
        return ans
    
    def min_start_value(self, nums) -> int:
        '''
        Given an array of integers nums, you start with an initial positive value startValue. In each iteration, you calculate the step by step sum of
        startValue plus elements in nums (from left to right). Return the minimum positive value of startValue such that the step by step sum is never less than 1.
        Input: nums = [-3,2,-3,4,2] prefix = [-3, -1, -4, 0, 2]
        Output: 5
        Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1. step by step sum
        startValue = 4 | startValue = 5 | nums
        (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
        (1 +2 ) = 3  | (2 +2 ) = 4    |   2
        (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
        (0 +4 ) = 4  | (1 +4 ) = 5    |   4
        (4 +2 ) = 6  | (5 +2 ) = 7    |   2
        '''
        start_val = 1
        while True:
            s = start_val
            failed = False
            for i in range(len(nums)):
                s += nums[i]
                if s < 1:
                    start_val += 1
                    failed = True
                    break
            if not failed:
                print(start_val)
                return start_val
            
    def k_radius_avg(self, nums, k) -> list[int]:
        '''
        You are given a 0-indexed array nums of n integers, and an integer k. The k-radius average for a subarray of nums centered at some index i 
        with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or 
        after the index i, then the k-radius average is -1.
        Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
        The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero,
        which means losing its fractional part.
        Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
        prefix = [7, 11, 14, 23, 24, 32, 37, 39, 45]
        Output: [-1,-1,-1,5,4,4,-1,-1,-1]
        Explanation:
        - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
        - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37. Using integer division, avg[3] = 37 / 7 = 5.
        - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
        - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
        - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
        '''
        prefix = [0] * len(nums)
        avg = [0] * len(nums)
        prefix[0] = nums[0]
        n = len(nums)
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        for i in range(n):
            if i < k or n - i - 1< k:
                 avg[i] = -1
            else:
                left = prefix[i - k - 1] if i - k -1 >= 0 else 0
                right = prefix[i + k]
                avg[i] = (right - left) // (2*k + 1)
        print(avg)
        return avg
    
    def reverse_words_in_string(self, s: str) -> str:
        '''
        Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
        and initial word order.
        Input: s = "Mr Ding"
        Output: "rM gniD"
        '''
        if not s:
            return ''
        left = 0
        ans = ''
        for right in range(len(s)):
            if s[right].isspace():
                ans += self.reverse_str(left, right - 1, s)
                left = right 
        ans += self.reverse_str(left, right, s)               
        print(ans)
        return ans
    
    def reverse_str(self, left, right, s):
        space = 0
        sub = s[left : right + 1]
        for i in range(len(sub)):
            if sub[i].isspace():
                space += 1
        reversed_s = sub[::-1].strip()
        result = " " * space + reversed_s 
        return result
    
    def reverse_only_letters(self, s: str) -> str:
        '''
        Given a string s, reverse the string according to the following rules: All the characters that are not English letters
        remain in the same position. All the English letters (lowercase or uppercase) should be reversed.
        Input: s = "a-bC-dEf-ghIj"
        reversed_s = jIhgfEdCba
        Output: "j-Ih-gfE-dCba"
        '''
        non_english_char_pos_dict = {}
        english_chars = []
        ans = []
        for i in range(len(s)):
            ascii_val = ord(s[i])
            if not self.is_english_alphabet(ascii_val=ascii_val):
               non_english_char_pos_dict[i] = s[i]
            else:
                english_chars.append(s[i])
        reversed_str = english_chars[::-1]
        english_i = 0
        for i in range(len(s)):
            non_english_char = non_english_char_pos_dict.get(i, None)
            if non_english_char:
                ans.append(non_english_char)
            else:
                english_char = reversed_str[english_i]
                ans.append(english_char)
                english_i += 1
        output = ''.join(ans)
        print(output)
        return output

    def is_english_alphabet(self, ascii_val) -> bool:
        return 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122
    

    def get_min_common(self, nums1, nums2) -> int:
        '''
        Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
        If there is no common integer amongst nums1 and nums2, return -1.
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]  
        '''
        i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                print(nums1[i1])
                return nums1[i1]
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        print("-1")
        return -1
    
    def move_zeros(self, nums):
        '''
        Input: nums = [0,1,0,3,12] 
        Output: [1,3,12,0,0]
        '''
        zero = non_zero = 0
        while zero < len(nums) and non_zero < len(nums):
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
                non_zero += 1
                zero += 1
            else:
                non_zero += 1
        return nums
    
    def reverse_prefix_of_word(self, s, ch) -> str:
        '''
        Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index
        of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

       if word = "abcdefd" and ch = "d", The resulting string will be "dcbaefd".
        '''
        first_idx = s.find(ch)
        if first_idx == -1:
            return s
        sub = s[0 : first_idx + 1]
        same = s[first_idx + 1 : len(s)]
        reversed_str = sub[::-1]
        output = reversed_str + same
        print(output)
        return output
    
    def minimum_length_subarray(self, target: int, nums: List[int]) -> int:
        '''
        Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
        sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        '''
        start = 0
        res = math.inf
        curr = 0
        n = len(nums)
        for i in range(n):
            curr += nums[i]
            while curr >= target and start < n:
                res = min(res, i - start + 1)
                curr -= nums[start]
                start += 1
        if res == math.inf:
            return 0
        else:
            return res
        
    def max_vowels(self, s: str, k: int) -> int:
        '''
        Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
        Input: s = "a b c i i i d e f", k = 3
        Output: 3
        Explanation: The substring "iii" contains 3 vowel letters.
        '''
        vowels = ['a', 'e', 'i', 'o', 'u']
        def vowel_count(word) -> int:
            tot = 0
            for w in word:
                if w in vowels:
                    tot += 1
            return tot

        start = 0
        curr = k - 1
        sub = s[start: curr + 1]
        ans = vowel_count(sub)
        temp = ans
        while curr < len(s) - 1:
            curr += 1
            if s[curr] in vowels:
                temp += 1 
            if s[start] in vowels:
                temp -= 1
            start += 1
            ans = max(ans, temp)
        return ans
    
    def equal_substring(self, s: str, t: str, max_cost: int) -> int:
        '''
        You are given two strings s and t of the same length and an integer maxCost. You want to change s to t.
        Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the
        ASCII values of the characters). Return the maximum length of a substring of s that can be changed to be the same as 
        the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can 
        be changed to its corresponding substring from t, return 0.
        Input: s = "abcd", t = "bcdf", maxCost = 3 Output: 3 Explanation: "abc" of s can change to "bcd".

        '''
        start = 0
        currentCost = 0
        maxLength = 0
        
        for end in range(len(s)):
            currentCost += abs(ord(s[end]) - ord(t[end]))
            
            while currentCost > max_cost:
                currentCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
    
    def largest_altitude(self, gain: List[int]) -> int:
        '''
        There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
        The biker starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length n 
        where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest 
        altitude of a point.
        Input: gain = [-5,1,5,0,-7] Output: 1 Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
        '''
        highest_alt = 0
        last = 0
        for i in range(len(gain)):
            last = last + gain[i]
            highest_alt = max(highest_alt, last)
        print(highest_alt)
        return highest_alt
    
    def pivot_index(self, nums: List[int]) -> int:
        '''
        Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the sum of 
        all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. 
        If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
        This also applies to the right edge of the array. Return the leftmost pivot index. If no such index exists, return -1.

        Input: nums = [1,7,3,6,5,6] Output:3
        '''
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
            # [1, 8, 11, 17, 22, 28]
        for i in range(len(prefix_sum)):
            left = 0 if i == 0 else prefix_sum[i - 1]
            right = 0 if i == len(prefix_sum) - 1 else prefix_sum[-1] - prefix_sum[i]
            if left == right:
                return i
        return -1

class NumArray:
    '''
    Input ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]  Output [null, 1, -1, -3]
    '''

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        # [-2, -2, 1, -4, -2, -3]
        self.prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sum[i] = nums[i] + self.prefix_sum[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)        
            





 


        

             
        
            

            




                


    


    

  






        
        


              