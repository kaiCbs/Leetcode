class Solution(object):
    def kClosest(self, points, K):
        return sorted(points,key=lambda x:x[0]**2 + x[1]**2)[:K]

# not good