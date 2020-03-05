class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        i,j,k = 0,1,len(nums)-1
        while k-i>1:
            new = nums[i]+nums[j]+nums[k]-target
            if new == 0:
                return target
            elif new > 0:
                k-=1
            else:
                j+=1                
            if abs(new) < abs(ans-target):
                ans = new+target  
            if k == j:
                i+=1
                j=i+1
                k= len(nums)-1
        return ans
