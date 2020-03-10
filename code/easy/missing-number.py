class Solution:
    def missingNumber(self, nums):
        res = 0
        for i,num in enumerate(nums):
            res ^= num^(i+1)
        return res

    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     return n*(n+1)//2 - sum(nums)

