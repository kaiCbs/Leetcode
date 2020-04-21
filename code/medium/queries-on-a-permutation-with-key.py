class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        P = list(range(1, m + 1))

        def move(l, i):
            return [l[i]] + l[:i] + l[i + 1:]

        for q in queries:
            idx = P.index(q)
            res.append(idx)
            P = move(P, idx)
        return res