class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def reverse(nums, j):
            nums[j:] = nums[j:][::-1]
            
        def find(nums, j):
            i = len(nums)-1
            while nums[i] <= nums[j]:
                i-=1
            nums[j], nums[i] = nums[i], nums[j]
            
        if len(nums) == 1: 
            return nums
        
        cur = len(nums)-1
        while nums[cur] <= nums[cur-1]:
            cur -= 1    
            if cur == 0:
                nums[:] = nums[::-1]
                return
            
        find(nums, cur-1)
        reverse(nums, cur)
