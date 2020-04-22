class Solution:
    def numOfWays(self, n: int) -> int:
        ans = 12
        res = [6, 6]
        maps = {1: [3, 2], 2: [2, 2]}
        for i in range(1, n):
            ans = (res[0] * 5 + res[1] * 4) % (10**9 + 7)
            res[0], res[1] = res[0] * 3 + res[1] * 2, res[0] * 2 + res[1] * 2
        return ans