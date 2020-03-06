from collections import Counter
class Solution(object):
    def commonChars(self, A):
        if not A:
            return []
        ans = Counter(A[0])
        for i in A[1:]:
            ans = (ans & Counter(i))
        return ans.elements()