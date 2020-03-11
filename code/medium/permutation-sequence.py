from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def helper(nums, k):
            s = factorial(len(nums)-1)
            m, k = (k-1)//s, (k-1)%s+1
            return nums.pop(m), k
        
        nums = [str(i+1) for i in range(n)]
        ans = ""
        while nums:
            s, k = helper(nums,k)
            ans = ans + s 
        return ans