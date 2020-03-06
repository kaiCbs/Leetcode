class Solution(object):
    def guessNumber(self, n, start = 1):
        """
        :type n: int
        :rtype: int
        """
        if n==start:
            return n
        num = (n+start)//2
        ans = guess(num)
        if ans==0:
            return num
        elif ans==-1:
            return self.guessNumber(num-1,start)
        else:
            return self.guessNumber(n,num+1)
            