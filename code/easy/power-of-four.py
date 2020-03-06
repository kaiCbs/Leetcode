class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<1:
            return False 
        while num>1:
            if num%4:
                return False
            num>>=2
        return True