class Solution(object):
    def sortedSquares(self, A):
        i,j = 0, len(A)-1
        k = len(A)-1
        ans = [0] * len(A)
        while i<j:
            if -(A[i]) < A[j]:
                ans[k] = A[j]**2
                j-=1
            else:
                ans[k] = A[i]**2
                i+=1
            k-=1
        ans[k] = A[i]**2
        return ans