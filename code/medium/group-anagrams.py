class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            ans.setdefault("".join(sorted(i)),[]).append(i)
        return ans.values()