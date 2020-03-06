class Solution(object):
    def peakIndexInMountainArray(self, A):
        w = len(A)
        if w == 3:
            return 1
        left, right = 0, w-1
        mid = (left + right)//2
        if A[mid-1]<A[mid]> A[mid+1]:
            return mid
        if A[mid] > A[mid+1]:
            return self.peakIndexInMountainArray(A[:mid+1])
        else:
            return mid + self.peakIndexInMountainArray(A[mid:])
        