class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mult = 1
        check = True
        while check:
            checker = True
            mult_k = k * mult
            for i in nums:
                if i == mult_k:
                    checker = False
                    break
            if checker:
                check = False
                break
            mult += 1
        return mult_k  