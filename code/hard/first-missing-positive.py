class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        N = len(nums)
        record = [0] * (N+1)
        for n in nums:
            try: 
                if n>0:
                    record[n-1] = 1
            except IndexError:
                pass
        for i in range(N+1):
            if not record[i]:
                return i+1
                