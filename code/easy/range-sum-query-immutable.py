class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumsum = [0]
        temp = 0
        for i in nums:
            temp += i
            self.cumsum.append(temp)    

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumsum[j+1] - self.cumsum[i] 
