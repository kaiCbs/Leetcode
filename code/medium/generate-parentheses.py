class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def GP(l, r, cum):
            if l == 0:
                return [')'*r]
            if cum == 0:
                return ['('+c for c in GP(l-1, r, cum+1)]
            else:
                return ['('+ c for c in GP(l-1, r, cum+1)] + [')'+ c for c in GP(l, r-1, cum-1)]  
        return GP(n,n,0)