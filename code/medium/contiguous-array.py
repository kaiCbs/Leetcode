class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cumsum, res = 0, {0: [-1]}
        nums = [i * 2 - 1 for i in nums]
        for i, n in enumerate(nums):
            cumsum += n
            res.setdefault(cumsum, []).append(i)
        return max([v[-1] - v[0] for v in res.values()])
