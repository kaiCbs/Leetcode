class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i,val in enumerate(nums):
            a = table.get(val)
            if a!=None and i - a <= k:
                return True
            table[val] = i
        return False