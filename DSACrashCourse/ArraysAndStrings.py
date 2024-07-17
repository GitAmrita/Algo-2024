from typing import List


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

        

             
        
            

            




                


    


    

  






        
        


              