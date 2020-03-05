class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ''
        base = strs[0]
        ans,i = '',0
        while i<len(base):
            ch = base[i]
            for st in strs[1:]:
                try:
                    if st[i]!=ch:
                        return ans
                except IndexError:
                    return ans
            ans+=ch
            i+=1
        return ans