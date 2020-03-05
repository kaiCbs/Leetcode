from functools import lru_cache

class Solution:
    @lru_cache(maxsize=50)
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1: return 1
        return self.uniquePaths(n-1,m) + self.uniquePaths(n,m-1)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         ans = 1
#         n, m = min(n,m), max(n,m)
#         for i in range(1,n):
#             ans *= (m-1+i)
#         for i in range(1,n):
#             ans /= i  
#         return int(ans)
# 
# Pure Math