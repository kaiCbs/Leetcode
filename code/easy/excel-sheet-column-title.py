class Solution(object):
    def convertToTitle(self, n):
        hashmap = {i:chr(i+65) for i in range(26)}
        ans = ""
        while n>0:
            ans += hashmap[(n-1)%26]
            n = (n-1)//26
        return ans[::-1]