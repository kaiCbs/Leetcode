class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "": return 0
        searchDict = {}
        i, j = 0,0
        searchDict[s[0]] = 0
        ans = 1
        while j<len(s)-1:
            j+=1
            if s[j] in searchDict:
                if (searchDict[s[j]]<i):
                    searchDict[s[j]] = j
                else:
                    i = searchDict[s[j]]+1
                    searchDict[s[j]] = j
            else:
                searchDict[s[j]] = j
            ans = max(ans,j-i+1)
        return ans