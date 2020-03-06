from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        freq = OrderedDict()
        for idx,l in enumerate(s):
            if l in freq:
                freq[l] = -1
            else:
                freq[l] = idx
        for a in freq:
            if freq[a]>-1:
                return freq[a]
        return -1