from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not (s and words):
            return []
        words_set = Counter(words)
        m, n = len(words), len(words[0])
        result = []    
        
        def helper(s):
            return Counter(s[i*n:i*n+n] for i in range(m)) == words_set  
        
        target = Counter("".join(words))
        init = Counter(s[:m*n])
        if init == target:
            if helper(s[:m*n]):
                result.append(0)      
                
        for i in range(0,len(s)-m*n):
            init[s[i]]-=1
            init[s[i+m*n]]+=1
            init += Counter()
            if init == target:
                if helper(s[i+1:i+1+m*n]):
                    result.append(i+1)         
        return result
                
# not good