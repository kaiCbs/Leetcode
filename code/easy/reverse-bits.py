class Solution:
    def reverseBits(self, n):
        a = "0b" + bin(n)[::-1][:-2]
        a += "0"*(34-len(a))
        return int(a,2)