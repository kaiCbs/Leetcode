class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [[r[i]for r in matrix[::-1]] for i in range(len(matrix))] 

# not good