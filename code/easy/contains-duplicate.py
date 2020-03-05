class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = 0
        return len(set(nums)) != len(nums)