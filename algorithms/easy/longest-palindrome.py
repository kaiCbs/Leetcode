from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        freq = Counter(s)
        ans, odd = 0, 0
        for l in freq:
            if freq[l]%2:
                odd = 1
                ans+=(freq[l]-1)
            else:
                ans+=freq[l]
        return ans+odd