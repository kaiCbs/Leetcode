class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def GCD(x, y): 
            while (y): 
                x, y = y, x % y 
            return x
        size = len(nums)
        loop = GCD(size,k)
        for i in range(loop):
            temp = nums[i]
            j = (i-k)%size
            nums[i] = nums[j]
            while j!=i:
                nums[j] = nums[(j-k)%size]
                j = (j-k)%size
            nums[(j+k)%size] = temp
