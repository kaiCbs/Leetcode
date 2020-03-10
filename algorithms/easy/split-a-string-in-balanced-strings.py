class Solution:
    def balancedStringSplit(self, s: str) -> int:
        hashmap = {'R':1,'L':-1}
        ans, count = 0, 0
        for i in s:
            count += hashmap[i]
            if count == 0:
                ans+=1
        return ans