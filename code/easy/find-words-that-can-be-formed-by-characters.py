from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        ans = 0
        alphabet = Counter(chars)
        for word in words:
            if Counter(word) == (alphabet & Counter(word)):
                ans+=len(word)
        return ans
        