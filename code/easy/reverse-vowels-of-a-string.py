class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in "aeiouAEIOU"]
        sl = list(s)
        for i,val in enumerate(s):
            if val in "aeiouAEIOU":
                sl[i] = vowels.pop()
        return "".join(sl)