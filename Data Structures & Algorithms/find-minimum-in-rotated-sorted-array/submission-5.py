from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        n = len(nums)

        if n == 1:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[0]