class Solution(object):
    def canJump(self, nums):
        if not nums:
            return true
        des = len(nums)-1
        nowMax = nums[0]
        nowId = 0
        while (nowMax<des) & (nowId < nowMax):
            nowId += 1
            if nowMax < nowId + nums[nowId]:
                nowMax = nowId + nums[nowId]
        return (nowMax>=des)
             