class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        N5, N10, N20 = 0, 0, 0
        for i in bills:
            if i == 5:
                N5+=1
            elif i == 10:
                N5 -= 1
                N10 += 1
            else:
                if N10>0:
                    N10-=1
                    N5-=1
                else:
                    N5-=3
            if N5<0 or N10<0:
                return False
        return True