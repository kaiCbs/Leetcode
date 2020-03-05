class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashs={}
        hasht={}
        cur = len(s)
        while cur>0:
            cur-=1
            cs = s[cur]
            ct = t[cur]
            if cs in hashs:
                if hashs[cs]!=ct:
                    return False
            else:
                hashs[cs] = ct
            if ct in hasht:
                if hasht[ct]!=cs:
                    return False
            else:
                hasht[ct] = cs
        return True