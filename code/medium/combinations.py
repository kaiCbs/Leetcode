class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==1:
            return [[i+1] for i in range(n)]
        elif n==k:
            return [list(range(1,k+1))]
        return [[n]+i for i in self.combine(n-1,k-1)] + self.combine(n-1,k)