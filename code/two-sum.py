class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            if num in h:
                return [i,h[num]]
            h[target-num] = i