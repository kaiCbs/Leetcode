class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        last = []
        for row in triangle:
            if last:
                row[0] += last[0]
                row[-1] += last[-1]
            for i in range(len(last)-1):
                row[i+1] = min(row[i+1]+last[i],row[i+1]+last[i+1])
            last = row
        return min(last)