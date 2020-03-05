class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = -1
        left = m-1  
        while nums2:
            a = nums2.pop()
            while (left>-1) and a < nums1[left] and (right != - (m+n)):
                nums1[right] = nums1[left]
                left -= 1
                right -=1
            nums1[right] = a
            right -= 1