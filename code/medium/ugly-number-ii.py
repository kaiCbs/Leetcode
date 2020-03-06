from bisect import insort
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        stack = [-1]
        record = {1}
        for i in range(n):
            s = -stack.pop()
            if s*2 not in record:
                bisect.insort(stack,-s*2)
                record.add(s*2)
            if s*3 not in record:
                bisect.insort(stack,-s*3)
                record.add(s*3)
            if s*5 not in record:
                bisect.insort(stack,-s*5)
                record.add(s*5)
        return s

## not good