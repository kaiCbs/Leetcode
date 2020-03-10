class Solution:
    def restoreIpAddresses(self, s: str, part = 4) -> List[str]:
        if part == 1:
            if s and -1<int(s)<256 and (s[0]!='0' or s=='0'):
                return [s]
            return []
        ans = []
        for i in range(1,4):
            ans+=[s[:i]+"."+sub for sub in self.restoreIpAddresses(s[i:],part=part-1)
                  if (s[:i] and -1<int(s[:i])<256 and (s[0]!='0' or i==1))]
        return ans