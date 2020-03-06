class Solution(object):
    def numJewelsInStones(self, J, S):
        return len([i for i in S if i in J])