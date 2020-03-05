class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        s = '*'+s
        dic = {(1,2):1}
        ans = s[1]
        i,j = 1,2
        hisLong, lastLongStart = (1,2), 1
        while j < len(s):
            dic[(j,j)], dic[(j,j+1)],dic[(j+1,j)] = 1, 1, 1
            cur = lastLongStart
            while not (dic[(cur,j)] and (s[cur-1] == s[j])):
                dic[(cur-1,j+1)] = 0
                cur+=1
            lastLongStart = max(cur,lastLongStart)-1
            dic[(lastLongStart,j+1)] = 1
            if (j+1-lastLongStart) > (hisLong[1]-hisLong[0]):
                hisLong = (lastLongStart,j+1)
            for m in range(cur+1,j+2):
                if (dic[(m,j)] and (s[m-1] == s[j])):
                    dic[(m-1,j+1)] = 1
                else:
                    dic[(m-1,j+1)] = 0
            j+=1
        return s[hisLong[0]:hisLong[1]]
        
# not good