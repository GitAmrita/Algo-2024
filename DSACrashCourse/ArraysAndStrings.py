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

                


    


    

  






        
        


              