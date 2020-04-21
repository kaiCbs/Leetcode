class Solution:
    def totalNQueens(self, n: int) -> int:

        global result
        result = 0

        def valid(i, placed):
            invalid = set([p + (i - j) for j, p in enumerate(placed)] +
                          [p - (i - j) for j, p in enumerate(placed)] + placed)
            all = set(range(n))
            return list(all - invalid)

        def helper(i, placed=[]):
            global result
            if i == n:
                result += 1
            else:
                for next in valid(i, placed):
                    helper(i + 1, placed + [next])

        helper(0, [])
        return result