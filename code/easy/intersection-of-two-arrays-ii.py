from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2 = Counter(nums1),Counter(nums2)
        intersect = (c1 & c2)
        result  = []
        for val in intersect:
            result.extend([val]*intersect[val])
        return result

# not good