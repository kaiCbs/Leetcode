class Solution:
    def isUgly(self, num: int) -> bool:
        for i in [2,3,5]:
            while num and not num%i:
                num //= i
        return num == 1    
            