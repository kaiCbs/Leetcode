class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1)+1, len(s2)+1
        path = [[0]*len2 for _ in range(len1)]
        for i in range(1,len1):
            for j in range(1,len2):
                path[i][j] = max(
                path[i-1][j],
                path[i][j-1],
                path[i-1][j-1] + int(s1[i-1]==s2[j-1])
                )
        return path[-1][-1]

# not good