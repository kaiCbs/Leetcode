class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: return s
        Key = sorted([(-abs((i%((numRows-1)*2))+1-numRows),i) for i in range(len(s))])
        return ''.join([s[i[1]] for i in Key])

# The ZigZag has a pattern with length 2*row-1