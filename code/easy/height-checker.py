class Solution(object):
    def heightChecker(self, heights):
        N = len(heights)
        return sum([sorted(heights)[i]!=heights[i] for i in range(N)])