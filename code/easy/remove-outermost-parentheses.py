class Solution(object):
    def removeOuterParentheses(self, S):
        stack = []
        ans = ''
        for i in S:
            if not stack:
                stack.append(i) 
            elif (stack == ['(']) and (i==')'):
                stack.pop()
            else:
                if i==')':
                    stack.pop()
                if i=='(':
                    stack.append(i)
                ans += i
        return ans
            