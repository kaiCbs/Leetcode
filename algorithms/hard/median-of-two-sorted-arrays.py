class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2,sp1=0,sp2=0,l1=0,l2=0):
        if l1+l2==0:
            l1,l2 = len(nums1),len(nums2)
        def mid(num,sp,l):
            midValue = (num[sp+l//2]+num[sp+(l-1)//2])/2
            return midValue
        if (l1>l2+4):
            sp1 +=(l1-l2-1)//2
            l1 -= ((l1-l2-1)//2) * 2
        elif (l2>l1+4):
            sp2 += (l2-l1-1)//2
            l2 -= ((l2-l1-1)//2) * 2
        while (l1+l2)>10:
            minl = min(l1,l2)
            shorten = (minl+1)//2-1
            if mid(nums1, sp1, l1) < mid(nums2, sp2, l2):
                return self.findMedianSortedArrays(nums1, nums2,sp1=sp1+shorten,sp2=sp2,l1=l1-shorten,l2=l2-shorten)
            elif mid(nums1, sp1, l1) > mid(nums2, sp2, l2):
                return self.findMedianSortedArrays(nums1, nums2,sp1=sp1,sp2=sp2+shorten,l1=l1-shorten,l2=l2-shorten)
            else:
                return mid(nums1, sp1, l1)
        new = sorted(nums1[sp1:sp1+l1]+nums2[sp2:sp2+l2])
        return mid(new,0,l1+l2)

# not good