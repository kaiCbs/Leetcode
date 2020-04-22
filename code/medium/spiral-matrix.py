class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        i, j, di, dj = 0, 0, 0, 1
        for number in range(1, len(matrix) * len(matrix[0]) + 1):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i + di) % len(matrix)][(j + dj) %
                                              len(matrix[0])] == None:
                di, dj = dj, -di
            i += di
            j += dj
        return res