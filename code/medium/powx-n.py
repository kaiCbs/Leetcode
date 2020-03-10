class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        ans = 1
        while n>0:
            x_p,p = x,1
            while 2*p <= n:
                p*=2
                x_p = x_p * x_p
            ans *= x_p
            n -= p
        return ans
        
        # if n==0:
        #     return 1
        # if n==1:
        #     return x
        # return self.myPow(x,n//2)*self.myPow(x,n//2)*self.myPow(x,n%2)