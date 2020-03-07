from functools import lru_cache
class Solution(object):
    def match(self, s, p, i, j):
        if i == len(s) or j == len(p):
            return False     
        return p[j] in ['.',s[i]]
    
    @lru_cache(100)
    def isMatch(self, s, p, i=0, j=0):
        if j==len(p):
            return i==len(s)
        if j < len(p)-1 and p[j+1] == "*":
            return (self.match(s,p,i,j) and self.isMatch(s, p, i+1, j)) or self.isMatch(s, p, i, j+2)
        if self.match(s,p,i,j):
            return self.isMatch(s,p,i+1,j+1)

# not good