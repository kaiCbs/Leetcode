class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(numbers):
            if num in h:
                return sorted([i+1,h[num]+1])
            h[target-num] = i