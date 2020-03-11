from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        cum, dic = 0, {}
        for num in sorted(freq.keys()):
            dic[num] = cum
            cum += freq[num]
        return [dic[i] for i in nums]
