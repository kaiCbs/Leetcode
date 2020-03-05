import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def nCr(n,r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)
        return [nCr(rowIndex,i) for i in range(rowIndex+1)]