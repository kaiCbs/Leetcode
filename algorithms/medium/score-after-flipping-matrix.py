class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        ans = len(A)
        if not A or not A[0]:
            return 0
        for i in A:
            if i[0] == 0:
                i[::] =  [1 - k for k in i]
        for j in range(len(A[0])-1):
            ans *= 2
            print(ans)
            count = sum([r[j+1] for r in A])
            ans += max(len(A)-count,count)
            print(ans)
        return ans
