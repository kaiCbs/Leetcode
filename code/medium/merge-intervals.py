class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for itv in intervals[1:]:
            if itv[0]<=ans[-1][1]:
                ans[-1][1] = max(itv[1],ans[-1][1])
            else:
                ans.append(itv)
        return ans