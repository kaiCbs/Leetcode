from string import punctuation
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = [i.lower() for i in s if i not in punctuation+' ']
        return l==l[::-1]