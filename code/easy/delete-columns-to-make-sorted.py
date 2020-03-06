class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A or not A[0]:
            return 0
        ans = 0
        for i in range(len(A[0])):
            flag = 0
            for j in range(len(A)-1):
                if A[j][i] > A[j+1][i]:
                    flag = 1
                    break
            ans += flag        
        return ans