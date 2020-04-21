class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def toStr(placed):
            res = []
            for Q in placed:
                res.append("." * (Q) + "Q" + "." * (n - Q - 1))
            return res

        def valid(i, placed):
            invalid = set([p + (i - j) for j, p in enumerate(placed)] +
                          [p - (i - j) for j, p in enumerate(placed)] + placed)
            all = set(range(n))
            return list(all - invalid)

        def helper(i, placed=[]):
            if i == n:
                result.append(toStr(placed))
            else:
                for next in valid(i, placed):
                    helper(i + 1, placed + [next])

        helper(0, [])
        return result