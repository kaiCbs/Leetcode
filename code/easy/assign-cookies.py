class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, ans = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i+=1
                j+=1
                ans+=1
            else:
                j+=1
        return ans

# not good