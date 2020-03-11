class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 1
        while num>1:
            ans += 1 + (num%2)
            num >>= 1
        return ans
