class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lth = len(grid)
        A = [max(l) for l in grid]
        B = [max([l[i] for l in grid]) for i in range(lth)]
        
        result = 0
        for i in range(lth):
            for j in range(lth):
                result += (min(A[i],B[j])-grid[i][j])
        return result