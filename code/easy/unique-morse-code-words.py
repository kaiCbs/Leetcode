class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = set()
        for w in words:
            s = ''
            for c in w:
                s += morse[ord(c)-97]
            a.add(s)
        return len(a)