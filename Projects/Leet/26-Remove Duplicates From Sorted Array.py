class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        index = 0
        count = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index+1]:
                nums.pop(index+1)
            else:
                count += 1
                index += 1
        count += 1
        return count