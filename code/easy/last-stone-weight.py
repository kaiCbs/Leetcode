import bisect 
class Solution:
    def lastStoneWeight(self, stones: List[int], f=1) -> int:
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]
        if f:
            stones.sort()
            f = 0
        smash = stones.pop()-stones.pop()
        bisect.insort(stones, smash)
        return self.lastStoneWeight(stones,f=f)