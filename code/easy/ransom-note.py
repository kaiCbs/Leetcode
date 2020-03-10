from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = Counter(ransomNote)
        m = Counter(magazine)
        return not (r-m)

# not good