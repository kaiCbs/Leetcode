class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 
               'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if s[i]+s[i+1] in ['IV','IX','XL','XC','CD','CM']:
                ans -= dic[s[i]]
            else:
                ans += dic[s[i]]
        ans += dic[s[-1]]
        return ans