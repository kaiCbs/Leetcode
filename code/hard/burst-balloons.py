from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        @lru_cache(len(nums)**2)
        def helper(i, j):
            res = 0
            if i > j:
                return 0
            for k in range(i,j+1):
                res = max(res, nums[i-1]*nums[k]*nums[j+1]+helper(i,k-1)+helper(k+1,j))
            return res
        return helper(0, len(nums)-2)