class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
        
#         if not nums: return 0
#         maxsub = [0,0,nums[0]]
#         for n in nums:
#             maxsub[0] = (max(maxsub[0],0) + n)
#             maxsub[1] = max(maxsub[1],maxsub[0],n)
#             maxsub[2] = max(maxsub[2],n)
#         if maxsub[2] < 0:
#             return maxsub[2]
#         return max(maxsub)
    
    