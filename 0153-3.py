## 2020/12/11

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid-1]: return nums[mid]
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]