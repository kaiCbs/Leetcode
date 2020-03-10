class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<2:
            return N
        return self.fib(N-1)+self.fib(N-2)
