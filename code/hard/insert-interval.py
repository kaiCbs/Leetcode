class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        def helper(i1, i2):
            if not i2:
                return -1
            if not i1:
                return 7
            if i1[1] <= i2[1] and i1[0] >= i2[0]:
                return 0
            elif i2[1] <= i1[1] and i2[0] >= i1[0]:
                return 1
            elif i1[1] < i2[0]:
                return 3
            elif i2[1] < i1[0]:
                return 4
            elif i1[1] >= i2[0] >= i1[0]:
                return 5
            else:
                return 6

        res = []
        for itv in intervals:
            s = helper(itv, newInterval)
            if s == 1:
                return intervals
            if s == 3 or s == -1:
                res.append(itv)
            if s == 5:
                newInterval[0] = itv[0]
            if s == 6:
                newInterval[1] = itv[1]
            if s == 4:
                res.append(newInterval)
                res.append(itv)
                newInterval = []
        if newInterval:
            res.append(newInterval)
        return res
