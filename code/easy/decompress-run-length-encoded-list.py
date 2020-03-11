from itertools import chain
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
       return chain.from_iterable(
           [i]*j for i,j in zip(nums[1::2],nums[::2])
       )