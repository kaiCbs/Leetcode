class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pace = {'L':1,'R':-1,'U':2**0.5,'D':-2**0.5}
        return -0.001 <(sum([pace[i] for i in moves])) < 0.001