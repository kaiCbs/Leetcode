class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def dd(divd,divi):
            ans = 0
            scaledDivisor = divi
            scale = 1
            while divd>=divi:
                if divd>=scaledDivisor:
                    divd-=scaledDivisor
                    ans+=scale
                    scaledDivisor += scaledDivisor
                    scale += scale
                else:
                    scaledDivisor//=2
                    scale//=2
            return ans
        if dividend*divisor==0:
            return 0
        elif dividend*divisor>0:
            return min(2**31-1,dd(abs(dividend),abs(divisor)))
        else:
            return max(-2**31,-dd(abs(dividend),abs(divisor)))