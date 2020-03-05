class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums:
            return self.subsets(nums[1:]) + [[nums[0]] + i for i in self.subsets(nums[1:])]
        return [[]]

# not good