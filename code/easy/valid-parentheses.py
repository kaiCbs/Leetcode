class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if stk and stk[-1]+i in ['{}','[]','()']:
                stk.pop()
            else:
                stk.append(i)
        return not stk