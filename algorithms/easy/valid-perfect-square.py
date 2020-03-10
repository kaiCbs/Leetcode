class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def mySqrt(x: int) -> int:
            if x<2:
                return x
            r = x
            while (r * r) > x:
                a = (r*r-x)//(2*r)
                if a==0:
                    break
                r-=a
            return r-1
        return mySqrt(num)**2 == num