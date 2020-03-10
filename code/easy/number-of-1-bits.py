class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        while n>0:
            ans += n%2
            n>>=1
        return ans