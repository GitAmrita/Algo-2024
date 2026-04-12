def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = list()
    for pivot, _ in enumerate(nums):
        if pivot > 0 and nums[pivot] == nums[pivot - 1]:
            continue
        left = pivot + 1
        right = len(nums) - 1
        while left < right:
            num_needed = nums[pivot] * -1
            if nums[left] + nums[right] == num_needed:
                result.append([nums[pivot], nums[left], nums[right]])
                left = left + 1
                right = right - 1
                while left < right and nums[left - 1] == nums[left]:
                    left = left + 1
                while left < right and nums[right + 1] == nums[right]:
                    right = right - 1
            elif nums[left] + nums[right] < num_needed:
                left = left + 1
            else:
                right = right - 1
    return result
