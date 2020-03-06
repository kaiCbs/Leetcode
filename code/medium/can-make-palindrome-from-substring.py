class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        count = [0 for i in range(26)]
        path = [count[::]]
        for ch in s:
            count[ord(ch)-97] += 1
            path.append(count[::])
        def valid(query):
            l,r = query[0],query[1]
            tol = [1 for i in range(26) if (path[r+1][i]-path[l][i])%2]
            if (l-r+1)%2 + 2*query[2] < sum(tol):
                return False
            return True
        return [valid(q) for q in queries]