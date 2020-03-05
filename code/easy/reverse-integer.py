class Solution:
    def reverse(self, x: int) -> int:
        a = [1,-1][x<0]*int(str(abs(x))[::-1])
        if a<-2**31 or a>2**31-1:
            return 0
        return a