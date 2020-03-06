from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        return list(Counter(t)-Counter(s))[0]

# not good