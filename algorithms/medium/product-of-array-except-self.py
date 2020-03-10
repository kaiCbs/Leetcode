class Solution(object):
    def productExceptSelf(self, nums):
        prod = 1
        zeros = 0
        for i in nums:
            if i!=0:
                prod *= i
            else:
                zeros+=1
        if zeros>1:
            return [0 for i in nums]
        elif zeros == 1:
            return [prod if i==0 else 0 for i in nums]
        else:
            return [prod//i for i in nums]
