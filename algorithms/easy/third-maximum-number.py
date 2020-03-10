class Solution(object):
    def thirdMax(self, nums):
        def update(max3, new):
            if len(max3)<3:
                return sorted(max3+[new],reverse=True)
            else:
                return sorted(max3+[new],reverse=True)[:3]
        ans = []
        nums = set(nums)
        for n in nums:
            ans = update(ans,n)
        if len(ans)<3:
            return ans[0]
        return ans[2]