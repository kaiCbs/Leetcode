from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a=0
        for i,val in enumerate(secret):
            if val == guess[i]:
                a+=1
        b=sum((Counter(secret)&Counter(guess)).values())-a
        return "%dA%dB"%(a,b)