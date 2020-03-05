class Solution(object):
    def rob(self, nums):
        if len(nums)<2:
            return sum(nums)
        money = [nums[0],nums[1]]
        for i in range(len(nums)-2):
            money = [max(money[0],money[1]), (money[0]+nums[i+2])]
        return max(money)

# not good