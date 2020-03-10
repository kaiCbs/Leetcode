class Solution(object):
    def uniqueOccurrences(self, arr):
        ans = {}
        for num in arr:
            ans[num] = ans.setdefault(num,0) + 1  
        return len(ans) == len(set(ans.values()))