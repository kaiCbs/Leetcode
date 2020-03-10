class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        if len(nums)<4:
            return ans
        def threeSum(nums,target):
            res = []
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l, r = i+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < target:
                        l +=1 
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
            return res
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ans += [[nums[i]] + sum3 for sum3 in threeSum(nums[i+1:],target-nums[i])]
        return ans