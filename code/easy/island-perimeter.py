class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def helper(coord):
            i, j = coord
            if not grid[i][j]:
                return 0
            return (
                int(j == col - 1 or grid[i][j + 1] == 0)
                + int(i == row - 1 or grid[i + 1][j] == 0)
                + int(j == 0 or grid[i][j - 1] == 0)
                + int(i == 0 or grid[i - 1][j] == 0)
            )

        return sum(
            map(helper, [(i, j) for i in range(row) for j in range(col)])
        )

