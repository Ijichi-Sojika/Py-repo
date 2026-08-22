class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if(j <= i):
                    continue
                else:
                    if(nums[i] + nums[j] == target):
                        res = list((i, j))
        
        return res