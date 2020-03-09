# mark
class Solution:
    def longestValidParentheses(self, s):
        stk, r = [[-1, ')']], 0
        for i, paren in enumerate(s):
            if paren == ')' and stk[-1][1] == '(':
                stk.pop()
                r = max(r, i - stk[-1][0])
            else:
                stk += [i, paren],
        return r
