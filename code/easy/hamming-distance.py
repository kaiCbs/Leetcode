class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x==y:
            return 0
        return self.hammingDistance(x//2, y//2) + (x-y)%2