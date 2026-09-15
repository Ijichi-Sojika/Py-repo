class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if len(nums) == 0:
                break
            if nums[index] == val:
                nums.pop(index)
                removed = True
            else:
                index += 1
        return len(nums)