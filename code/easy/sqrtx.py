class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        r = x
        while (r * r) > x:
            a = (r*r-x)//(2*r)
            if a==0:
                break
            r-=a
        return r-1