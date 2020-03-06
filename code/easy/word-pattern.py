class Solution:
    def wordPattern(self, pattern: str, Str: str) -> bool:
        a,b,c=set(),set(),set()
        Str = Str.split()
        if len(Str)!=len(pattern):
            return False
        for i,val in enumerate(pattern):
            a.add(val)
            b.add(val+Str[i])
            c.add(Str[i])
        return len(a) == len(b) == len(c)