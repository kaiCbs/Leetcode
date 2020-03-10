class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair = 0
        while n>=0:
            stair+=1
            n-=stair
        return stair-1

# not good