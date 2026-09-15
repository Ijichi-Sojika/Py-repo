class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            res = len(nums) - 1
            return res
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i