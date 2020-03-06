class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = []
        for i in S:
            if not ans:
                ans.append(i)
            elif ans[-1] + i == '()':
                ans.pop()
            else:
                ans.append(i)
        return len(ans)