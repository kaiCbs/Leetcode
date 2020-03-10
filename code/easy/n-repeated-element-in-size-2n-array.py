class Solution(object):
    def repeatedNTimes(self, A):
        a = {}
        for i in A:
            if i in a:
                return i
            else:
                a[i] = 1