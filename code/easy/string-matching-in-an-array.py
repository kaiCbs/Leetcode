class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words = sorted(words, key=len)
        for i, w in enumerate(words):
            for ot in words[i + 1:]:
                if w in ot:
                    res.append(w)
                    break
        return res
